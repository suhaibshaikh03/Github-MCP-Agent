from dotenv import load_dotenv, find_dotenv
import os
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
from agents.mcp.server import MCPServerStreamableHttp, MCPServerStreamableHttpParams
from agents.mcp import create_static_tool_filter
import chainlit as cl

# Load environment variables
_ = load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
token = os.getenv("GITHUB_TOKEN")

# MCP server parameters
tool_filter = create_static_tool_filter(allowed_tool_names=[
"get_me",
"get_teams",
"search_repositories",
"create_repository",
"list_repos",
"list_issues",
"create_issue",
"update_issue",
"add_issue_comment",
"search_issues",
"list_pull_requests",
"create_pull_request",
"merge_pull_request",
"add_comment_to_pending_review",
"list_workflows",
"run_workflow",
"rerun_workflow_run",
"list_workflow_runs",
"list_notifications",
"mark_all_notifications_read",
"list_projects",
"add_project_item",
"get_file_contents",
"create_or_update_file"
])
mcp_params = MCPServerStreamableHttpParams(
    url='https://api.githubcopilot.com/mcp/',
    headers={
        "Authorization": "Bearer " + token
    }
)

@cl.on_chat_start
async def handle_chat_start():
    try:
        # Initialize MCP server client
        mcp_server_client = await MCPServerStreamableHttp(params=mcp_params, name="MySharedMCPServerClient",tool_filter=tool_filter).__aenter__()
        cl.user_session.set("mcp_server_client", mcp_server_client)

        # Initialize GitHub agent
        github_agent = Agent(
            name="GitHub Agent",
            instructions="""
            You are a specialized GitHub agent with comprehensive capabilities for managing GitHub repositories, issues, pull requests, and workflows.
            You have access to my github's MCP server from where you can read data and perform operations on my github repositories.

            ## Core Capabilities:
            ### Repository Management:
            - Create, clone, and manage repositories
            - Handle branches, tags, and releases
            - Manage repository settings, collaborators, and permissions
            - Work with repository contents (files, directories, commits)

            ### Issue & Pull Request Management:
            - Create, update, and close issues
            - Manage pull requests (create, review, merge)
            - Handle labels, milestones, and assignees
            - Comment on issues and pull requests

            ### Code Operations:
            - Read, create, update, and delete files
            - Handle commits and commit history
            - Manage branches and merges
            - Work with GitHub Actions workflows

            ### Collaboration:
            - Manage team members and permissions
            - Handle code reviews and approvals
            - Work with GitHub organizations
            - Manage webhooks and integrations

            ## Guidelines:
            1. Always verify repository access and permissions before operations
            2. Use descriptive commit messages and issue titles
            3. Follow GitHub best practices for branching and merging
            4. Be helpful in explaining GitHub concepts and workflows
            5. Provide clear feedback on operation results
            6. Handle errors gracefully and suggest solutions

            ## Response Format:
            - Provide clear, actionable responses
            - Include relevant GitHub URLs when applicable
            - Explain complex operations step-by-step
            - Offer alternatives when operations fail

            You should be knowledgeable about GitHub's API, Git workflows, and best practices for collaborative development.
            """,
            mcp_servers=[mcp_server_client],
            model="gpt-4o-mini"
        )
        cl.user_session.set("github_agent", github_agent)
        cl.user_session.set("history", [])
        await cl.Message(content="Hello! I'm the GitHub Agent. How can I help you with your GitHub repositories today?").send()

    except Exception as e:
        print(f"Error setting up MCP server: {e}")
        # Fallback to basic agent without MCP
        github_agent = Agent(
            name="GitHub Agent",
            instructions="You are a GitHub agent. Please set up your GITHUB_TOKEN environment variable to enable full functionality."
        )
        cl.user_session.set("github_agent", github_agent)
        cl.user_session.set("history", [])
        await cl.Message(content="GitHub Agent is ready! Please configure your GITHUB_TOKEN for full functionality.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    github_agent = cl.user_session.get("github_agent")
    history = cl.user_session.get("history")
    msg = cl.Message(content="")
    await msg.send()
    history.append({"role": "user", "content": message.content})

    try:
        result = Runner.run_streamed(
            github_agent,
            input=history,
        )
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                await msg.stream_token(event.data.delta)

        history.append({"role": "assistant", "content": result.final_output})
        cl.user_session.set("history", history)

    except Exception as e:
        await cl.Message(content=f"Error processing request: {e}").send()

@cl.on_stop
async def handle_stop():
    mcp_server_client = cl.user_session.get("mcp_server_client")
    if mcp_server_client:
        await mcp_server_client.__aexit__(None, None, None)
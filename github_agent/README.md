# GitHub Agent

A powerful GitHub management agent built with the OpenAI Agents SDK. This agent can help you manage GitHub repositories, issues, pull requests, and more through natural language interactions.

## Features

### 🏗️ Repository Management
- Create and manage repositories
- Handle branches, tags, and releases
- Manage repository settings and permissions
- Work with repository contents and commits

### 🐛 Issue & Pull Request Management
- Create, update, and close issues
- Manage pull requests (create, review, merge)
- Handle labels, milestones, and assignees
- Comment on issues and pull requests

### 💻 Code Operations
- Read, create, update, and delete files
- Handle commits and commit history
- Manage branches and merges
- Work with GitHub Actions workflows

### 👥 Collaboration
- Manage team members and permissions
- Handle code reviews and approvals
- Work with GitHub organizations
- Manage webhooks and integrations

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd github-agent
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Set up your environment variables:
```bash
# Create a .env file
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

## Usage

### Running the Agent

Start the interactive GitHub agent:

```bash
python main.py
```

### Example Interactions

Once the agent is running, you can interact with it using natural language:

```
You: Create a new repository called "my-awesome-project"
GitHub Agent: I'll help you create a new repository called "my-awesome-project". Let me set that up for you...

You: Create an issue in my-awesome-project with the title "Add documentation"
GitHub Agent: I'll create an issue titled "Add documentation" in your my-awesome-project repository...

You: Show me all open pull requests in my-awesome-project
GitHub Agent: Let me fetch the open pull requests for your repository...
```

### Programmatic Usage

You can also use the agent programmatically:

```python
from main import github_agent, runner

# Run a single command
response = runner.run("Create a new branch called feature/new-feature")
print(response)

# Or use the agent directly
response = github_agent.run("List all repositories")
print(response)
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### GitHub Authentication

To perform GitHub operations, you'll need to configure GitHub authentication. The agent can work with:

- Personal Access Tokens
- GitHub Apps
- OAuth tokens

Make sure your GitHub credentials have the necessary permissions for the operations you want to perform.

## Example Commands

Here are some example commands you can try with the GitHub agent:

### Repository Management
- "Create a new repository called 'my-project'"
- "Clone the repository 'username/repo-name'"
- "List all my repositories"
- "Delete the repository 'old-project'"

### Issue Management
- "Create an issue in 'my-repo' with title 'Bug fix needed'"
- "List all open issues in 'my-repo'"
- "Close issue #123 in 'my-repo'"
- "Add label 'bug' to issue #123"

### Pull Request Management
- "Create a pull request from 'feature-branch' to 'main'"
- "List all open pull requests in 'my-repo'"
- "Merge pull request #456"
- "Review pull request #789"

### File Operations
- "Read the README.md file from 'my-repo'"
- "Create a new file 'script.py' in 'my-repo'"
- "Update the file 'config.json' in 'my-repo'"
- "Delete the file 'old-file.txt' from 'my-repo'"

## Development

### Project Structure

```
github-agent/
├── main.py          # Main agent implementation
├── pyproject.toml   # Project dependencies
├── README.md        # This file
└── uv.lock         # Dependency lock file
```

### Adding New Features

To extend the agent with new capabilities:

1. Add new tools to the `tools` list in the agent configuration
2. Update the agent instructions to include the new capabilities
3. Test the new functionality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Contact the maintainers

## Roadmap

- [ ] Add more GitHub API integrations
- [ ] Implement GitHub Actions workflow management
- [ ] Add support for GitHub organizations
- [ ] Create a web interface
- [ ] Add more advanced Git operations
- [ ] Implement repository templates


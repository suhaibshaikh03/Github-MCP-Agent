#!/usr/bin/env python3
"""
Example usage of the GitHub Agent

This script demonstrates how to use the GitHub agent programmatically
for various GitHub operations.
"""

from main import github_agent, runner

def example_usage():
    """Demonstrate various GitHub agent capabilities"""
    
    print("🤖 GitHub Agent Example Usage\n")
    
    # Example 1: Repository management
    print("1. Repository Management Examples:")
    examples = [
        "List all my repositories",
        "Create a new repository called 'test-repo'",
        "Get information about the repository 'username/repo-name'"
    ]
    
    for example in examples:
        print(f"   - {example}")
    
    print("\n2. Issue Management Examples:")
    issue_examples = [
        "Create an issue in 'my-repo' with title 'Bug in login'",
        "List all open issues in 'my-repo'",
        "Close issue #123 in 'my-repo'",
        "Add label 'bug' to issue #123 in 'my-repo'"
    ]
    
    for example in issue_examples:
        print(f"   - {example}")
    
    print("\n3. Pull Request Examples:")
    pr_examples = [
        "Create a pull request from 'feature-branch' to 'main' in 'my-repo'",
        "List all open pull requests in 'my-repo'",
        "Merge pull request #456 in 'my-repo'",
        "Review pull request #789 in 'my-repo'"
    ]
    
    for example in pr_examples:
        print(f"   - {example}")
    
    print("\n4. File Operations Examples:")
    file_examples = [
        "Read the README.md file from 'my-repo'",
        "Create a new file 'script.py' in 'my-repo'",
        "Update the file 'config.json' in 'my-repo'",
        "Delete the file 'old-file.txt' from 'my-repo'"
    ]
    
    for example in file_examples:
        print(f"   - {example}")
    
    print("\n" + "="*50)
    print("To run these examples, use the interactive mode:")
    print("python main.py")
    print("\nOr use the agent programmatically:")
    print("response = runner.run('Your command here')")

def run_single_command(command: str):
    """Run a single command with the GitHub agent"""
    try:
        print(f"Running command: {command}")
        response = runner.run(command)
        print(f"Response: {response}")
        return response
    except Exception as e:
        print(f"Error running command: {e}")
        return None

if __name__ == "__main__":
    # Show example usage
    example_usage()
    
    # Uncomment the line below to run a specific command
    # run_single_command("List all my repositories")


#!/usr/bin/env python3
"""
Build the README.md from the Jinja2 template.

This script:
- Fetches all public repositories from the jupyter-ai-contrib organization using PyGithub
- Reads stable.yaml for the list of stable repository names
- Generates README.md with stable and experimental sections
"""

import os
from pathlib import Path

import yaml
from github import Github, Auth
from jinja2 import Environment, FileSystemLoader


def fetch_public_repos(org_name: str) -> list[dict]:
    """Fetch all public repositories from a GitHub organization.

    Args:
        org_name: Name of the GitHub organization

    Returns:
        List of dicts with name, url, and description for each public repo
    """
    # Try to get GitHub token from environment (optional, but helps with rate limits)
    token = os.environ.get("GITHUB_TOKEN")

    if token:
        auth = Auth.Token(token)
        g = Github(auth=auth)
    else:
        g = Github()

    print(f"Fetching repositories from {org_name} organization...")

    org = g.get_organization(org_name)
    repos = []

    for repo in org.get_repos(type="public"):
        repos.append({
            "name": repo.name,
            "url": repo.html_url,
            "description": repo.description or ""
        })

    print(f"✓ Found {len(repos)} public repositories")

    return repos


def main():
    # Get the directory containing this script
    script_dir = Path(__file__).parent

    # Fetch all public repos from GitHub
    all_repos = fetch_public_repos("jupyter-ai-contrib")

    # Load stable.yaml
    stable_file = script_dir / "stable.yaml"
    with open(stable_file) as f:
        stable_data = yaml.safe_load(f)
        stable_names = set(stable_data.get("stable_repos", []))

    # Split repos into stable and experimental
    stable_repos = []
    experimental_repos = []

    for repo in all_repos:
        repo_data = {
            "name": repo["name"],
            "url": repo["url"],
            "description": repo["description"]
        }

        if repo["name"] in stable_names:
            stable_repos.append(repo_data)
        else:
            experimental_repos.append(repo_data)

    # Sort both lists alphabetically by name
    stable_repos.sort(key=lambda x: x["name"].lower())
    experimental_repos.sort(key=lambda x: x["name"].lower())

    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(script_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Load and render template
    template = env.get_template("README.jinja2.md")
    output = template.render(
        stable_repos=stable_repos,
        experimental_repos=experimental_repos
    )

    # Write output
    output_file = script_dir / "README.md"
    with open(output_file, "w") as f:
        f.write(output)

    print(f"✓ Generated README.md")
    print(f"  - Stable repositories: {len(stable_repos)}")
    print(f"  - Experimental repositories: {len(experimental_repos)}")


if __name__ == "__main__":
    main()

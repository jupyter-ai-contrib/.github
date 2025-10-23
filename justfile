# Justfile for managing the .github repository

# Default recipe - show available commands
default:
    @just --list

# Build the README.md from the Jinja2 template (fetches repos from GitHub)
build-readme:
    #!/usr/bin/env bash
    cd profile
    uv run build.py

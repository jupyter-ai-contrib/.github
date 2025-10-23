# Jupyter AI Contrib

Welcome to Jupyter AI Contrib!

The Jupyter AI Contrib organization contains a set of Jupyter extensions that are designed to enable humans and AI to collaborate together.

## Strategy

Our mission is to create modular, extensible building blocks that enable humans and AI to collaborate effectively in Jupyter environments. We focus on developing components that can be composed together to support a wide range of AI-assisted workflows, from code generation and data analysis to interactive learning and research.

To guide our work and ensure a cohesive ecosystem, we follow these guiding principles:

- **Production Ready** — We hold a high bar for performance, reliability, and long-term stability. Our components should be robust enough for real-world research, education, and enterprise workloads.
- **Exceptional User Experience** — We prioritize thoughtful interaction design, visual polish, and accessibility. Our tools should be intuitive, inclusive, and beautiful, working seamlessly for all users within the Jupyter ecosystem.
- **Composable, Modular Architecture** — We design reusable components that fit together cleanly, enabling users and developers to assemble AI workflows that meet their specific needs without monolithic tooling.

While Jupyter AI Contrib was created by leaders in the Jupyter community, it is not currently an [official Jupyter subproject](https://jupyter.org/governance/list_of_subprojects.html). However, we intend for this organization to become an official Jupyter AI subproject over time as we mature our governance, community, and technical foundations.

## Community

We welcome contributors of all backgrounds and skill levels! Whether you're fixing bugs, adding features, improving documentation, or sharing ideas, your contributions help make AI-assisted Jupyter workflows better for everyone. All community members are expected to follow the [Jupyter Code of Conduct](https://jupyter.org/governance/conduct/code_of_conduct.html).

Please join the community conversation on [GitHub Discussions](https://github.com/orgs/jupyter-ai-contrib/discussions) to ask questions, share ideas, or propose new features.

## Stable Repositories

We have marked the following repositories as being "stable". This status means the repos are, or are quickly becoming, stable and ready for production use.

- [**jupyter-ai-chat-commands**](https://github.com/jupyter-ai-contrib/jupyter-ai-chat-commands) - Default set of chat commands in Jupyter AI
- [**jupyter-ai-jupyternaut**](https://github.com/jupyter-ai-contrib/jupyter-ai-jupyternaut) - Package which provides the Jupyternaut, the default AI persona, in Jupyter AI
- [**jupyter-ai-litellm**](https://github.com/jupyter-ai-contrib/jupyter-ai-litellm) - LiteLLM based model abstraction for Jupyter AI
- [**jupyter-ai-persona-manager**](https://github.com/jupyter-ai-contrib/jupyter-ai-persona-manager) - The core manager & registry for AI personas in Jupyter AI
- [**jupyter-ai-router**](https://github.com/jupyter-ai-contrib/jupyter-ai-router) - The core routing layer used in Jupyter AI to process chat messages
- [**jupyter-ai-tools**](https://github.com/jupyter-ai-contrib/jupyter-ai-tools) - No description available
- [**jupyter-server-documents**](https://github.com/jupyter-ai-contrib/jupyter-server-documents) - Server side document handling with improved output handling and kernel management/status.
- [**jupyter-server-mcp**](https://github.com/jupyter-ai-contrib/jupyter-server-mcp) - An MCP interface/extension for Jupyter Server 
- [**jupyterlab-diff**](https://github.com/jupyter-ai-contrib/jupyterlab-diff) - JupyterLab commands to show cell and file diffs

## Experimental Repositories

These repositories are experimental and under active development:

- [**jupyter-ai-claude-code**](https://github.com/jupyter-ai-contrib/jupyter-ai-claude-code) - A Jupyter AI persona for Claude Code
- [**jupyter-ai-personas**](https://github.com/jupyter-ai-contrib/jupyter-ai-personas) - AI Personas for Jupyter AI
- [**jupyter-floating-chat**](https://github.com/jupyter-ai-contrib/jupyter-floating-chat) - A jupyterlab extension to add a floating chat input
- [**jupyter-server-ai-tools**](https://github.com/jupyter-ai-contrib/jupyter-server-ai-tools) - A Jupyter Server extension for discovering tools across extensions.
- [**jupyterlab-cell-input-footer**](https://github.com/jupyter-ai-contrib/jupyterlab-cell-input-footer) - JupyterLab Plugin that provides a cell input footer
- [**jupyterlab-commands-toolkit**](https://github.com/jupyter-ai-contrib/jupyterlab-commands-toolkit) - JupyterLab commands as an AI Toolkit
- [**jupyterlab-document-collaborators**](https://github.com/jupyter-ai-contrib/jupyterlab-document-collaborators) - No description available
- [**jupyterlab-magic-wand**](https://github.com/jupyter-ai-contrib/jupyterlab-magic-wand) - An in-cell AI assistant for JupyterLab notebooks
- [**jupyterlab-notebook-awareness**](https://github.com/jupyter-ai-contrib/jupyterlab-notebook-awareness) - Track current notebook and active cell in JupyterLab's awareness

## Governance

The organization is owned and governed by the following decision makers (in alphabetical order):

- [@ellisonbg](https://github.com/ellisonbg) - Brian Granger
- [@3coins](https://github.com/3coins) - Piyush Jain
- [@dlqqq](https://github.com/dlqqq) - David Qiu
- [@Zsailer](https://github.com/Zsailer) - Zach Sailer
- [@jtpio](https://github.com/jtpio) - Jeremy Tuloup

Jupyter AI Contrib follows a simple, consensus-seeking governance model designed to enable rapid iteration while maintaining quality and community input. We implement this by roughly following the [Jupyter Decision Making Guide](https://jupyter.org/governance/decision_making.html) with the above decision makers guiding the consusus seeking process and voting when needed.

Org-level decisions are made by majority vote of the org owners on [GitHub Discussions](https://github.com/orgs/jupyter-ai-contrib/discussions) using thumbs up 👍 and thumbs down 👎 reactions. These org-level decisions include new repository creation, promotion of repositories to "Stable" status, new org owners, etc.

---

*This README is automatically generated from `README.jinja2.md`. To update, modify `stable.yaml` or the template, then run `just build-readme`.*
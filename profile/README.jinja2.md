# Jupyter AI Contrib

Welcome to Jupyter AI Contrib!

The Jupyter AI Contrib organization contains a set of Jupyter extensions that are designed to enable humans and AI to collaborate together.

## Strategy

Our mission is to create modular, extensible building blocks that enable humans and AI to collaborate effectively in Jupyter environments. We focus on developing components that can be composed together to support a wide range of AI-assisted workflows, from code generation and data analysis to interactive learning and research.

Jupyter AI Contrib is not currently an [official Jupyter subproject](https://jupyter.org/governance/list_of_subprojects.html), but we intend for this organization to become a new Jupyter AI subproject over time as we mature our governance, community, and technical foundations.

## Community

We welcome contributors of all backgrounds and skill levels! Whether you're fixing bugs, adding features, improving documentation, or sharing ideas, your contributions help make AI-assisted Jupyter workflows better for everyone.

- **Code of Conduct**: All community members are expected to follow the [Jupyter Code of Conduct](https://github.com/jupyter/governance/blob/main/conduct/code_of_conduct.md).
- **Discussions**: Join the conversation on [GitHub Discussions](https://github.com/orgs/jupyter-ai-contrib/discussions) to ask questions, share ideas, or propose new features.

## Stable Repositories

These repositories are considered stable and ready for production use:

{% for repo in stable_repos %}
- [**{{ repo.name }}**]({{ repo.url }}) - {{ repo.description or "No description available" }}
{% endfor %}

## Experimental Repositories

These repositories are experimental and under active development:

{% for repo in experimental_repos %}
- [**{{ repo.name }}**]({{ repo.url }}) - {{ repo.description or "No description available" }}
{% endfor %}

## Governance

Jupyter AI Contrib follows a simple, consensus-seeking governance model designed to enable rapid iteration while maintaining quality and community input.

### Decision Makers

The organization is governed by the following decision makers (in alphabetical order):

- [@blink1073](https://github.com/blink1073) - Jeremy Tuloup
- [@davidbrochart](https://github.com/davidbrochart) - David Qiu
- [@ellisonbg](https://github.com/ellisonbg) - Brian Granger
- [@piyushjain27](https://github.com/piyushjain27) - Piyush Jain
- [@Zsailer](https://github.com/Zsailer) - Zach Sailer

### Decision-Making Process

Decisions are made by majority vote on [GitHub Discussions](https://github.com/orgs/jupyter-ai-contrib/discussions) using thumbs up 👍 and thumbs down 👎 reactions. This includes both organization-level decisions and decisions within individual repositories.

### Organization-Level Decisions

The following decisions require organization-level approval:

- **New repository creation and transfers**: Adding new repositories to the organization or transferring repositories in/out
- **Promotion of repositories to "Stable" status**: Moving repositories from Experimental to Stable
- **New owners/decision makers**: Adding or removing decision makers from the governance team

### Repository Governance

Individual repositories use the same consensus-seeking model with the five decision makers as the ultimate authorities. Repository-level decisions (features, bug fixes, releases, etc.) are made through pull requests and issues with input from contributors and approval from decision makers.

---

*This README is automatically generated from `README.jinja2.md`. To update, modify `stable.yaml` or the template, then run `just build-readme`.*

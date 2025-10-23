# Jupyter AI Contrib

The Jupyter AI Contrib organization contains a set of Jupyter extensions that are designed to enable humans and AI to collaborate together.

## Building profile/README.md

The org-level README.md file that is shown [here](https://github.com/jupyter-ai-contrib) is located in the file `profile/README.md`. This file is generated from a template at `profile/README.jinja2.md`. To build the actual `profile/README.md` file, you will need to install `uv` and `just`:

```bash
brew install uv just
```

Then you can build the `profile/README.md` by doing:

```bash
just build-readme
```

You should do this anytime you edit the template or when you want to update the data from the repos.
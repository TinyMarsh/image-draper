# Image Draper

[![Test and build](https://github.com/TinyMarsh/image-draper/actions/workflows/ci.yml/badge.svg)](https://github.com/TinyMarsh/image-draper/actions/workflows/ci.yml)

## Usage

1. Create and activate a Virtual Environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate # with Powershell on Windows: `.venv\Scripts\Activate.ps1`
   ```

2. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main app:

   ```bash
   python -m image_draper
   ```

## Development

This is a Python application that uses [`pip-tools`] for packaging and dependency management. It also provides [`pre-commit`](https://pre-commit.com/) hooks for [ruff](https://pypi.org/project/ruff/) and automated tests using [`pytest`](https://pytest.org/) and [GitHub Actions](https://github.com/features/actions). Pre-commit hooks are automatically kept updated with a dedicated GitHub Action.

[`pip-tools`] is chosen as a lightweight dependency manager that adheres to the [latest standards](https://peps.python.org/pep-0621/) using `pyproject.toml`.

Setup your environment by installing dependencies from `dev-requirements.txt`.

### Updating Dependencies

To add or remove dependencies:

1. Edit the `dependencies` variables in the `pyproject.toml` file (aim to keep develpment tools separate from the project requirements).
2. Update the requirements files:
   - `pip-compile` for `requirements.txt` - the project requirements.
   - `pip-compile --extra dev -o dev-requirements.txt` for `dev-requirements.txt` - the development requirements.
3. Sync the files with your installation (install packages):
   - `pip-sync dev-requirements.txt requirements.txt`

To upgrade pinned versions, use the `--upgrade` flag with `pip-compile`.

Versions can be restricted from updating within the `pyproject.toml` using standard python package version specifiers, i.e. `"black<23"` or `"pip-tools!=6.12.2"`

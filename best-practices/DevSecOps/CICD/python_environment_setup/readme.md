# Poetry

## Challenge

If we install from pyproject.toml using pip,  there is no way to install the dev dependencies.

## Solution

[Recreate environment using Poetry](https://github.com/tloeber/sagemaker-pipelines-abstraction/blob/41f794586b918b0ec99c24b0de1ca5e5fd5d9bdf/.github/workflows/python-package.yml).

- I used Github Actions from the Marketplace to simplify caching etc, but it should be easy to implement directly (the builtin `setup-python` also allows caching for Poetry). I found [this blog post](https://jacobian.org/til/github-actions-poetry/) helpful.

### Problems encountered

- Can't activate environment with `poetry shell` (at least in GitHub Actions, but I think it may be about Docker containers in general).
  - Could use `poetry run` for every command, but I wanted to be able to reuse the `make` commands that I also use for local development, in order to avoid drift.
  - Solution: `Set virtualenvs-in-project: true`, then we can simply activate  the environment by running `source .venv/bin/activate`.

## Alternatives considered

- Tried exporting all requirements from lockfile to a requirements.txt using [Poetry's export functionality](https://github.com/python-poetry/poetry-plugin-export) (see [here](https://github.com/tloeber/sagemaker-pipelines-abstraction/blob/4c01b86409ff547b89cdd467436325adddc792d0/.github/workflows/python-package.yml#L57)). Unfortunately, I encountered some bugs, as it kept missing some of the dependencies.
- Of course, it is also possible to install dev dependencies individually, but  it is better to avoid this is possible because:
  - This is more complicated to maintain, especially if you want to make sure that we use the same versions of the crucial data packages for local development and in the pipeline.
  - Even worse, this is risky because pip-installing additional packages may change the versions of non-dev packages, and may thus alter the behavior of the production code.

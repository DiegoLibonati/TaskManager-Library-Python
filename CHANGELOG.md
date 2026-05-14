# CHANGELOG


## v0.1.0 (2026-05-14)

### Bug Fixes

- __init__.py added to models test folder
  ([`07f69e7`](https://github.com/DiegoLibonati/propel/commit/07f69e7d9860ba337115a5e77a29f9a9eae2c52c))

- Better repository name/description and better system test
  ([`14924c9`](https://github.com/DiegoLibonati/propel/commit/14924c93a1bb3ff3a6633e56be2fc49b4eee7310))

- Better tests
  ([`66b93fb`](https://github.com/DiegoLibonati/propel/commit/66b93fb074951691475aabd86ccf9c508d775d97))

- Fix files names
  ([`1392403`](https://github.com/DiegoLibonati/propel/commit/1392403dd609add44cc9c257d775f13948636423))

- Fix models name
  ([`fa4c62e`](https://github.com/DiegoLibonati/propel/commit/fa4c62e05321f20c48059cc9dc9f9e7a6785c295))

- Pip version to fix vulnerabilities and ci updated
  ([`0a950bf`](https://github.com/DiegoLibonati/propel/commit/0a950bfdc3d43cca78875217f9c71a9f6bbd1a70))

- Pre-commit fix lint
  ([`e2ba0ba`](https://github.com/DiegoLibonati/propel/commit/e2ba0ba96e97e5bae78f8db98828df4c087f713e))

- Remove migrations exclude in pre commit config and update requirements dev
  ([`b900a66`](https://github.com/DiegoLibonati/propel/commit/b900a661f9a3fa1bf3aba497ed37f33a8bfd21e9))

- Rename model files
  ([`7a7c9d9`](https://github.com/DiegoLibonati/propel/commit/7a7c9d9e4a41401cb71c89edaa26af42cfa398ea))

- Title app
  ([`269aac3`](https://github.com/DiegoLibonati/propel/commit/269aac3a3510a1ae4f462ff64b19b8b5725bf3af))

### Continuous Integration

- Add automated changelog and versioning with python-semantic-release
  ([`7648889`](https://github.com/DiegoLibonati/propel/commit/7648889d006954665c8d54d5e2db3e58148885c3))

- Split single job into lint-and-audit, testing, and build
  ([`0c58213`](https://github.com/DiegoLibonati/propel/commit/0c582138ab6b0cdc27a59a1b6eb6ec6c2fe0541e))

Replaces the monolithic lint-and-build job with three chained jobs: lint-and-audit runs ruff and
  pip-audit on Python 3.13; testing runs pytest with coverage across the 3.11/3.12/3.13 matrix;
  build produces the distribution and asserts the .tar.gz artifact exists.

### Features

- .gitignore added
  ([`7665b59`](https://github.com/DiegoLibonati/propel/commit/7665b59adf36712a7a58b56118f9ac988786aa79))

- .python-version file added
  ([`e5ddf76`](https://github.com/DiegoLibonati/propel/commit/e5ddf761208a0f7411fc99b7de05229d51fcc97c))

- Better readme
  ([`f39cc3b`](https://github.com/DiegoLibonati/propel/commit/f39cc3bad44e38415d8de9f13bb25551f90fd97b))

- Build with setuptools added
  ([`44d9632`](https://github.com/DiegoLibonati/propel/commit/44d96328856cc6e0c9fd510ac3658459ea51e47a))

- Migrate dependencies to pyproject.toml extras and add CI pipeline
  ([`734ab77`](https://github.com/DiegoLibonati/propel/commit/734ab7738e3d8f7a4fcf1311607ec1f4e4245ab4))

Consolidate dev/test dependencies into [project.optional-dependencies] groups and redirect
  requirements files to editable installs, add a GitHub Actions workflow running ruff lint, build
  and pip-audit across Python 3.11–3.13, ship a py.typed marker for PEP 561 compliance, expose
  __version__ via importlib.metadata, add .editorconfig for cross-editor consistency, and fix
  BaseError to use None sentinels so subclass-level code/message defaults are honored when no
  argument is passed.

- New conftest added and better structure tests
  ([`2c703d9`](https://github.com/DiegoLibonati/propel/commit/2c703d9b5da205287f4f3365382b6b8bff315358))

- New properties in TaskManager Class
  ([`7835726`](https://github.com/DiegoLibonati/propel/commit/7835726757484cb479a0f054879b47e1c9bd0b5d))

- Pre-commit added
  ([`7e0905d`](https://github.com/DiegoLibonati/propel/commit/7e0905d7ea7c5168dd35935e2566ded56a642a57))

- Refactor of template library python
  ([`028c182`](https://github.com/DiegoLibonati/propel/commit/028c182eb5e41fb2581e85cd17a84eb88dcd7748))

- Tests added
  ([`1f7762d`](https://github.com/DiegoLibonati/propel/commit/1f7762d34c3b58ee0a51cbaf57bf81d03103f6bc))

### Refactoring

- Replace inline mains with examples/ demo package
  ([`4c424b7`](https://github.com/DiegoLibonati/propel/commit/4c424b7e33dbea37301fb009528985929b0153c3))

- Remove main() + __main__ blocks from manager.py and task_model.py - Add examples/demo.py
  showcasing the full propel API (add, move state, edit, log) - Register propel-demo console script
  in pyproject.toml

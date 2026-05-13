# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `py.typed` marker so consumers' type checkers honor inline annotations (PEP 561).
- Top-level `__version__` attribute on the `propel` package, read from installed metadata.
- `project.urls` and richer classifiers in `pyproject.toml` (3.12, 3.13, `Typing :: Typed`).
- `[project.dependencies]` and `[project.optional-dependencies]` (`dev`, `test`) in `pyproject.toml`.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) running lint, build and `pip-audit`.
- `.editorconfig` for cross-editor consistency.
- `CHANGELOG.md` (this file).

### Changed

- `BaseError.__init__` now uses `None` sentinels so subclass-level `code` / `message` overrides are honored when no argument is passed.
- Tightened Ruff rule set (added `B`, `SIM`, `RUF`, `C4`).
- `[tool.setuptools.packages.find]` now explicitly includes `propel*`.
- `.gitignore` defensively ignores `.venv/` and `env/`.

### Removed

- Per-file `requirements*.txt` install steps superseded by `pip install -e .[dev,test]`.

## [1.0.0] - 2026-05-12

### Added

- Initial public release of the `propel` library.
- `Manager` class orchestrating task lifecycle operations (`add_task`, `remove_task`, `edit_task`, `move_task_by_state`, `logging_task`).
- `TaskModel` domain object with immutable UUID and validated state transitions.
- Typed exception hierarchy (`ValidationError`, `NotFoundError`, `ConflictError`, `BusinessError`, `AuthenticationError`, `InternalError`) inheriting from `BaseError`.
- `setup_logger` factory with handler deduplication.

[Unreleased]: https://github.com/DiegoLibonati/TaskManager-Library-Python/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/DiegoLibonati/TaskManager-Library-Python/releases/tag/v1.0.0

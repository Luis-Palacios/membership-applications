# Copilot Instructions

## Project state and commands

- This is an early-stage Python 3.14 project managed with `uv`; use `uv sync` to install the root project and workspace dependencies.
- Build the root package with `uv build`.
- Lint with `uv run ruff check .`. Ruff uses a 110-character limit and additionally enforces annotation, async, type-checking-import, naming, security, and import-sorting rules.
- Type-check with `uv run ty check`.
- There is no test suite or test runner configured yet, so no full-suite or single-test command exists. When tests are introduced, add the corresponding `uv run <runner> path/to/test.py::test_name` command here.
- `uv run membership-applications` invokes the placeholder `membership_applications.main()`. To exercise the existing membership-application query flow, use `uv run python -m membership_applications.cli.main`.
- The API is a separate uv workspace member at `src/membership_applications/api`; keep its FastAPI dependency and configuration in that member's `pyproject.toml`.

## Architecture

- The repository's implemented functionality is the assimilation data layer for the existing SQL Server database, plus a CLI and a preliminary membership-applications FastAPI surface. This is a single microservice; `docs/ARCHITECTURE.md` describes its architecture and `docs/ROADMAP.md` tracks the sequence.
- `data/assimilation/config.py` loads settings from `.env`; importing the data layer requires `ASSIMILATION_DATABASE_URL`. Copy `.env.example` for local configuration and never commit credentials.
- `database.py` owns the SQLAlchemy engine, `SessionLocal`, and declarative `Base`. Callers own session lifetime: the CLI uses a context manager, while FastAPI uses the `get_assimilation_db` yield dependency.
- Keep SQLAlchemy table mappings, selectable query builders, and application-facing services separate:
  - Models map the legacy SQL Server schema exactly, including its original table and column casing.
  - `queries.py` constructs typed `Select` expressions.
  - `service.py` applies business/query-window behavior and returns typed `NamedTuple` results.
  - `query_helpers.py` maps selected columns into a dataclass or `NamedTuple`; aliases and selected column names must exactly match its constructor field names.
- The recent-applications service determines the 30-day window relative to the newest persisted application, falling back to the current UTC time if none exists. Preserve that behavior unless deliberately changing the feature contract.
- The FastAPI approval/rejection endpoints are placeholders; they do not yet persist status changes or publish the future membership-approval event.

## Repository conventions

- Use modern SQLAlchemy 2.x declarative typing (`Mapped`, `mapped_column`, `relationship`) and explicit `Session` annotations.
- Keep imports used only for annotations behind `TYPE_CHECKING`, matching the existing data-layer pattern.
- Use `from __future__ import annotations` in modules that need forward references without runtime imports.
- Query service result types are `NamedTuple` classes rather than ORM instances, so API and CLI callers consume only the projected fields.
- Treat `docs/ARCHITECTURE.md` as a target design, not evidence that container deployment, caching, logging, or notifications already exist.

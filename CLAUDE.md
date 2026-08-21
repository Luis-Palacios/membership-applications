# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

Early-stage: no tests or CI yet, but real code exists beyond the placeholder entry point. Treat architecture notes below as provisional — update this file as real structure gets added.

This is one of three planned microservices in a larger system (membership applications, roles/auth, small-group reports) sitting alongside a future Next.js client. See `docs/ARCHITECTURE.md` for the target end-state design and `docs/ROADMAP.md` for near-term plan — don't inline that detail here; this file should stay short since it's loaded into every agent session.

## Commands

This project uses [uv](https://docs.astral.sh/uv/) with the `uv_build` backend (Python >=3.14, pinned via `.python-version`).

- Sync dependencies / create the venv: `uv sync`
- Run the console script (currently just the placeholder `main()`): `uv run petra-smallgroups`
- Run the actual membership-applications CLI logic: `uv run python -m petra_smallgroups.cli.main`
- Build the package: `uv build`
- Lint: `uv run ruff check .` (config in `ruff.toml`); pre-commit hooks are set up via `.pre-commit-config.yaml`

## Architecture

- Packaging: `pyproject.toml` defines a console script `petra-smallgroups` that maps to `petra_smallgroups:main` (still the placeholder — not yet wired to real logic).
- `src/petra_smallgroups/cli/main.py` — the actual working code so far: queries membership applications generated in the last 30 days from the assimilation DB.
- `src/petra_smallgroups/data/assimilation/` — SQLAlchemy data layer for the existing SQL Server DB (the "assimilation" system):
  - `config.py` — pydantic-settings `Settings`, loaded from `.env` (see `.env.example`; requires `ASSIMILATION_DATABASE_URL`).
  - `database.py` — SQLAlchemy `engine`, `SessionLocal`, declarative `Base`.
  - `models/membership_applications/` — the `MembershipApplication` model (maps to existing `MemberShipApplications` table) plus its query builders in `queries.py`.
- Open design question (see `docs/ROADMAP.md`): whether to wrap this data layer in a repository abstraction before FastAPI is added on top, or call SQLAlchemy directly from API routes.

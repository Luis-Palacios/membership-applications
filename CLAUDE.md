# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

Early-stage: no tests or CI yet, but real code exists beyond the placeholder entry point. Treat architecture notes below as provisional — update this file as real structure gets added.

This is a single microservice for membership applications, sitting alongside an existing church web application. See `docs/ARCHITECTURE.md` for this service's architecture and `docs/ROADMAP.md` for near-term plan — don't inline that detail here; this file should stay short since it's loaded into every agent session.

## Commands

This project uses [uv](https://docs.astral.sh/uv/) with the `uv_build` backend (Python >=3.14, pinned via `.python-version`).

- Sync dependencies / create the venv: `uv sync`
- Run the console script (currently just the placeholder `main()`): `uv run membership-applications`
- Run the actual membership-applications CLI logic: `uv run python -m membership_applications.cli.main`
- Run the FastAPI development server: `uv run --package membership-applications-api fastapi dev src\membership_applications\api\main.py`
- Run the FastAPI production-style server: `uv run --package membership-applications-api fastapi run src\membership_applications\api\main.py`
- Build the package: `uv build`
- Lint: `uv run ruff check .` (config in `ruff.toml`); pre-commit hooks are set up via `.pre-commit-config.yaml`

Run commands from the repository root so the data layer loads the root `.env`.

## Architecture

- Packaging: `pyproject.toml` defines a console script `membership-applications` that maps to `membership_applications:main` (still the placeholder — not yet wired to real logic).
- `src/membership_applications/cli/main.py` — the actual working code so far: queries membership applications generated in the last 30 days from the assimilation DB.
- `src/membership_applications/data/assimilation/` — SQLAlchemy data layer for the existing SQL Server DB (the "assimilation" system):
  - `config.py` — pydantic-settings `Settings`, loaded from the root `.env` when commands run from the repository root (see `.env.example`; requires `ASSIMILATION_DATABASE_URL`).
  - `database.py` — SQLAlchemy `engine`, `SessionLocal`, declarative `Base`.
  - `models/membership_applications/` — the `MembershipApplication` model (maps to existing `MemberShipApplications` table) plus its query builders in `queries.py`.
- Open design question (see `docs/ROADMAP.md`): whether to wrap this data layer in a repository abstraction before FastAPI is added on top, or call SQLAlchemy directly from API routes.

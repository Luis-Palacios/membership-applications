# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

This is an early-stage skeleton: a single placeholder entry point (`src/petra_smallgroups/__init__.py`) with no tests, lint config, or CI yet. Treat architecture notes below as provisional — update this file as real structure gets added.

## Commands

This project uses [uv](https://docs.astral.sh/uv/) with the `uv_build` backend (Python >=3.14, pinned via `.python-version`).

- Run the CLI entry point: `uv run petra-smallgroups`
- Sync dependencies / create the venv: `uv sync`
- Build the package: `uv build`

## Architecture

- Packaging: `pyproject.toml` defines a console script `petra-smallgroups` that maps to `petra_smallgroups:main`.
- Source layout: `src/petra_smallgroups/` — the `main()` function in `__init__.py` is currently the only code in the project.

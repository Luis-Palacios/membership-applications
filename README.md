# Membership Applications

A Python microservice for reviewing membership applications, built alongside an existing church web application. Currently implemented: the SQL Server data layer, a CLI, and a FastAPI surface for membership applications.

## Overview

This project serves three objectives:

1. Learning exercise to get up to date with the latest Python stack (primary objective — self-funded, no cost pressure)
2. Learning agentic workflows (GitHub Copilot + Claude Code) during development, working toward an actual agentic dev workflow
3. Real working software, adding a new component (this API) alongside an existing church web app rather than extending it — used by a small real user base (~20 people)

Architecture notes: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Near-term plan: [docs/ROADMAP.md](docs/ROADMAP.md).

## What's built so far

- **Data layer** (`src/membership_applications/data/assimilation/`) — SQLAlchemy models, queries, and service for the existing SQL Server (assimilation) database.
- **CLI** (`src/membership_applications/cli/main.py`) — queries membership applications from the last 30 days and prints them.
- **API** (`src/membership_applications/api/`) — FastAPI workspace member with endpoints to list recent applications and placeholder approve/reject endpoints.

## Plan for next steps

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Main packages

- **SQLAlchemy** — ORM for the existing SQL Server database
- **FastAPI** — REST API for membership applications
- **Pydantic / pydantic-settings** — settings management and request/response schemas

## Requirements

1. Python 3.14
2. uv

## Setup

1. `uv sync` — installs root package and workspace dependencies (including the FastAPI workspace member)
2. Copy the root `.env.example` to the root `.env` and set `ASSIMILATION_DATABASE_URL`

## Running

Run these commands from the repository root so they load the root `.env`.

```powershell
# CLI — list recent membership applications
uv run python -m membership_applications.cli.main

# FastAPI dev server — use this for day-to-day local development.
# Auto-reloads on file changes; binds 127.0.0.1:8000; does NOT read
# PORT / keep-alive / graceful-shutdown from .env (fastapi dev doesn't expose those).
uv run --package membership-applications-api fastapi dev src\membership_applications\api\main.py

# FastAPI production-style server — no auto-reload. Use this to run/test the app
# the way it'll behave in staging, production, or Docker (reads PORT, keep-alive
# and graceful-shutdown timeouts from .env; binds 0.0.0.0).
uv run --package membership-applications-api python -m membership_applications.api.run
```

Request/DB timeouts (connect, query, pool, request, keep-alive, graceful-shutdown, port) are all configurable via `.env` — see `.env.example` for the full list and defaults.

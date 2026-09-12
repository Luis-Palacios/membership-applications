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

## Configuration notes

- **DB connection pool** (`DB_POOL_SIZE`, `DB_MAX_OVERFLOW`) — total connections a single process can hold against SQL Server. Once running as multiple containers, the real ceiling is `(WORKERS x replica count) x (DB_POOL_SIZE + DB_MAX_OVERFLOW)`, and this DB is shared with the existing church web app, so that total needs headroom, not just to stay under SQL Server's hard cap.
- **`WORKERS`** — uvicorn worker processes in `run.py`. Raising this multiplies the DB pool ceiling above *and* silently changes rate limiting: `slowapi`'s limiter (`src/membership_applications/api/rate_limit.py`) counts in-memory per process, so a "10/minute" route limit becomes "10 x WORKERS per minute" with no error to flag it. Leave at `1` and scale via container replica count once deployed behind an orchestrator (ECS/K8s) instead.

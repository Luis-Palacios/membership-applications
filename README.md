# Petra Small Groups Management

A Python project building three microservices alongside an existing church web application. Currently implemented: the SQL Server data layer, a CLI, and a FastAPI surface for membership applications.

## Overview

This project serves three objectives:

1. Learning exercise to get up to date with the latest Python stack (primary objective — self-funded, no cost pressure)
2. Learning agentic workflows (GitHub Copilot + Claude Code) during development, working toward an actual agentic dev workflow
3. Real working software, adding new components (APIs, Next.js front-end, new Postgres DB) alongside an existing church web app rather than extending it — used by a small real user base (~20 people)

Full target architecture (three microservices, two databases, messaging, deployment): [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## What's built so far

- **Data layer** (`src/petra_smallgroups/data/assimilation/`) — SQLAlchemy models, queries, and service for the existing SQL Server (assimilation) database.
- **CLI** (`src/petra_smallgroups/cli/main.py`) — queries membership applications from the last 30 days and prints them.
- **Membership Applications API** (`src/petra_smallgroups/membership_applications_api/`) — FastAPI workspace member with endpoints to list recent applications and placeholder approve/reject endpoints.

## Plan for next steps

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Main packages

- **SQLAlchemy** — ORM for the existing SQL Server database
- **FastAPI** — REST API for membership applications (Microservice 1)
- **Pydantic / pydantic-settings** — settings management and request/response schemas

## Requirements

1. Python 3.14
2. uv

## Setup

1. `uv sync` — installs root package and workspace dependencies (including the FastAPI workspace member)
2. Copy `.env.example` to `.env` and set `ASSIMILATION_DATABASE_URL`

## Running

```bash
# CLI — list recent membership applications
uv run python -m petra_smallgroups.cli.main

# FastAPI dev server — membership applications API
uv run fastapi dev src/petra_smallgroups/membership_applications_api/main.py
```

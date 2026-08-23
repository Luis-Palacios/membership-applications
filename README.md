# Petra Small Groups Management

This repo will contain the fast api and flask api to handle new members applications and small groups list and reports, for now I'm working
on the data layer and small cli to quickly test

## Overview

This project serves three objectives:

1. Learning exercise to get up to date with the latest Python stack (primary objective — self-funded, no cost pressure)
2. Learning agentic workflows (GitHub Copilot + Claude Code) during development, working toward an actual agentic dev workflow
3. Real working software, adding new components (APIs, Next.js front-end, new Postgres DB) alongside an existing church web app rather than extending it — used by a small real user base (~20 people)

Full target architecture (three microservices, two databases, messaging, deployment): [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

## Plan for next steps

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Main packages

1) Alchemy
2) FastAPI
3) Flask
4) Celery

## Requirements

1. Python 3.14
2. uv

## Setup

1) `uv sync`
2) Setup your own `.env` file

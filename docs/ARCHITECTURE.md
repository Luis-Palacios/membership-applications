# Architecture (target / vision)

This describes where the project is headed, not what's built yet — for current implementation state, see the root `CLAUDE.md`.

## System shape

Three microservices behind a single Next.js client, replacing/augmenting an existing church web application (SQL Server DB, real users) by adding new components alongside it rather than extending it directly.

### Microservice 1 — Membership applications (assimilation)
- Uses the **existing SQL Server DB** via SQLAlchemy (this is the code that exists today, under `src/petra_smallgroups/data/assimilation/`).
- FastAPI surface to list, review, and approve membership applications.

### Microservice 2 — Roles & authentication
- Also reads the existing SQL Server DB (church member/role data: small-group leader, deacon, elder, etc.).
- Owns a **new Postgres DB** for new authentication (users, roles) — new auth should live on the new DB, not the legacy one.
- Creates actual user accounts and links them to existing church-member roles.
- Subscribes to a message/event from Microservice 1 when a membership application is approved, and upgrades the applicant to a member.

### Microservice 3 — Small group reports
- Uses **only** the new Postgres DB.
- New tables for small-group leaders to submit weekly reports, review them, and manage small groups (assign leaders, manage membership rosters, etc.).

### Client
- Single Next.js app consuming all three APIs.

## Infra / deployment target
- Docker → Kubernetes → Terraform, deployed to AWS or GCP.
- Basic CI/CD, likely GitHub Actions.
- Messaging/eventing between services (mechanism TBD) for the Microservice 1 → Microservice 2 approval handoff.
- Caching and logging as cross-cutting concerns (mechanism TBD).
- Notifications: email and WhatsApp.

## Why this shape
This is primarily a learning project (modern Python/FastAPI/Flask stack, agentic dev workflows with Claude Code, eventually a real deployed multi-service system) that also needs to work for a small real user base (~20 people at one church). The three-microservice split follows the natural data-ownership boundaries: legacy SQL Server data Microservice 1 and 2 read, vs. new Postgres data that auth (Microservice 2) and small-group reporting (Microservice 3) own.

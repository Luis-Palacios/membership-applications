# Roadmap (near-term)

This is lightweight scaffolding, not the full detailed implementation plan (that comes later). See `docs/ARCHITECTURE.md` for the target end-state this is working toward.

## Next steps
1. Implement FastAPI endpoints on top of the existing `data/assimilation` module (Microservice 1).
2. **Open decision:** does the data module need an actual repository abstraction to decouple FastAPI from SQLAlchemy, or is calling SQLAlchemy directly from routes fine here? Weigh against how much this is a learning exercise vs. a small app that doesn't need the extra layer.
3. Implement authentication and authorization (start of Microservice 2 — new Postgres DB for auth).
4. Implement the Next.js front-end, starting with viewing membership applications.
5. Basic automated deploy on push (GitHub Actions).

## Not started / later
- Microservice 2's role-linking (church roles ↔ new auth) and the approval-event subscription from Microservice 1.
- Microservice 3 (small-group reports) entirely.
- Docker/Kubernetes/Terraform deployment.
- Messaging, caching, logging, email/WhatsApp notifications.

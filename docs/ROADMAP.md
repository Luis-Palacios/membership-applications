# Roadmap (near-term)

This is lightweight scaffolding, not the full detailed implementation plan (that comes later). See `docs/ARCHITECTURE.md` for the target end-state this is working toward.

## Next steps
1. FastAPI endpoints on top of the existing `data/assimilation` module: `GET /applications/recents` is implemented (reuses the CLI's service layer). `POST /applications/approve` and `/applications/reject` exist but are placeholders — they don't persist status changes or publish the future membership-approval event yet.
2. **Open decision, revisit:** routes currently call `services.py` functions directly (no repository abstraction). This works fine so far; revisit only if the service layer stops being a sufficient seam between FastAPI and SQLAlchemy. Weigh against how much this is a learning exercise vs. a small app that doesn't need the extra layer.
3. Basic automated deploy on push (GitHub Actions).

## Not started / later
- Docker/Kubernetes/Terraform deployment.
- Caching, logging, email/WhatsApp notifications.

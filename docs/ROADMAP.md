# Roadmap (near-term)

This is lightweight scaffolding, not the full detailed implementation plan (that comes later). See `docs/ARCHITECTURE.md` for the target end-state this is working toward.

## Next steps
1. Implement FastAPI endpoints on top of the existing `data/assimilation` module.
2. **Open decision:** does the data module need an actual repository abstraction to decouple FastAPI from SQLAlchemy, or is calling SQLAlchemy directly from routes fine here? Weigh against how much this is a learning exercise vs. a small app that doesn't need the extra layer.
3. Basic automated deploy on push (GitHub Actions).

## Not started / later
- Docker/Kubernetes/Terraform deployment.
- Caching, logging, email/WhatsApp notifications.

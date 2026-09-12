import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from membership_applications.api.config import api_settings
from membership_applications.api.dependencies import SessionDep
from membership_applications.api.logging_config import configure_logging
from membership_applications.api.middleware import (
    RequestLoggingMiddleware,
    RequestTimeoutMiddleware,
)
from membership_applications.api.rate_limit import limiter
from membership_applications.api.routers import applications, people
from membership_applications.data.assimilation.config import settings

configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Membership Applications API",
    description="API for managing membership applications, review and approval process",
    summary="API for managing membership applications",
    version="1.0.0",
    debug=settings.debug,
    docs_url="/docs" if settings.environment == "local" else None,
    redoc_url="/redoc" if settings.environment == "local" else None,
    openapi_url="/openapi.json" if settings.environment == "local" else None,
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    RequestTimeoutMiddleware, timeout_seconds=api_settings.request_timeout_seconds
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=api_settings.cors_allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)
app.add_middleware(RequestLoggingMiddleware)
app.include_router(applications.router)
app.include_router(people.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Membership Applications API!"}


@app.get("/health")
@limiter.exempt
def health_check(db: SessionDep) -> dict[str, str]:
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        logger.exception("Health check failed: database unreachable")
        raise HTTPException(status_code=503, detail="Database unreachable")
    return {"status": "ok"}

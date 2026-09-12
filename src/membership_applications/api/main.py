from fastapi import FastAPI

from membership_applications.api.routers import applications, people

app = FastAPI(
    title="Membership Applications API",
    description="API for managing membership applications, review and approval process",
    summary="API for managing membership applications",
    version="1.0.0",
)
app.include_router(applications.router)
app.include_router(people.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Membership Applications API!"}

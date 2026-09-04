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


# @app.on_event("startup")
# def startup_event() -> None:
#     print("Starting up the Membership Applications API...")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Membership Applications API!"}

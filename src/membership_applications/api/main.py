from fastapi import FastAPI

from membership_applications.api.routers import applications

app = FastAPI()
app.include_router(applications.router)


# @app.on_event("startup")
# def startup_event() -> None:
#     print("Starting up the Membership Applications API...")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Membership Applications API!"}

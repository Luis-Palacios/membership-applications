# Petra Small Groups Management
This repo will contain the fast api and flask api to handle new members applications and small groups list and reports, for now I'm working
on the data layer and small cli to quickly test

## Plan for next steps
1. Implement FastAPI that uses the data module to query the db
2. Figure out if I want to make the data module an actual repository to abstract fastapi from sqlalchemy will this be worht it or will it be just additional code
2. Implement authentication and authorization

## Main packages
1) Alchemy
2) FastAPI
3) Flask
4) Celery
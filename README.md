# Petra Small Groups Management
This repo will contain the fast api and flask api to handle new members applications and small groups list and reports, for now I'm working
on the data layer and small cli to quickly test

## Overview
This project will serve three objectives:
1. Learning exercise for me to get up to date with python latest stack
    - This objective is the primary one since I'm doing it for free and will pay for infrastructure my self
    - Will implement three microservices, tree api, two databases, messages, cache, logging, email and whatsapp notifications, etc
        - Microservice 1 will use existing DB via sqlalchemy and use fast as API to show membership applications, review and approve them
        - Microservice 2 will also use existing DB, will allow reviewing members and roles within the church such as small group leader, deacon, elder, I will need to find a 
        way to link these roles with a new authtentication I need to create, ideally this
        microservice will also allow creating actual users and roles so maybe this one will also use the new postgres db since new authentication should be on new db, and also here we should subscribe to message when Microservice 1 approve a membership application
        here we will upgrade people to members
        - Microservice 3 should only use the new DB, here we will have new tables in order for
        leaders of small groups to submit their weekly small group reports, review them and manage small groups, (set leaders, set members, etc)
    - Will implement a single nextjs client that uses all three APIs
    - Will use docker and then kubernetes and then terraform to deploy everything into AWS or GCP
    - Will need a Devops pipeline maybe github actions
2. Learning agentic workflows, I have a github copilot subscription and a claude code subscription I want to use agents the best I could during development and then move all the 
way to having an actual agentic workflow
3. An actual working software that builds on top of an existing web application being used by real user from a church with sql server db by adding new features but instead of extending the existing web application it add new components (api, front-end (nextjs), new postgres DB, etc )
    - All of this will actually be used by real people, it will probably be around 20 users without much demand and while everything I'm doing is overkill for this use case I will do 
    it as learning


## Plan for next steps
1. Implement FastAPI that uses the data module to query the db
2. Figure out if I want to make the data module an actual repository to abstract fastapi from sqlalchemy will this be worht it or will it be just additional code
3. Implement authentication and authorization
4. Implement front-end with nextjs to start seeing membership applications
5. Do a very basic automated deploy on push

## Main packages
1) Alchemy
2) FastAPI
3) Flask
4) Celery
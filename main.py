import os
from dotenv import load_dotenv
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

if ENVIRONMENT == "local":
    load_dotenv(".env.local")
elif ENVIRONMENT == "dev":
    load_dotenv(".env.dev")
from fastapi import FastAPI, HTTPException
from Models.VehicleIncidentModel import *
from Models.UserModel import *
from Services.Incidents import *
from DatabaseLayer.db import init_db
from Services.Exceptions.IncidentExceptions import *
from WebTransportRegistration.Services.IncidentRegister import register_exception_handlers
from fastapi import Depends
from AuthHandler.JWTHandler import get_current_user



init_db()  # Initialize the database when the application starts

app = FastAPI() 

register_exception_handlers(app)  # Register custom exception handlers

@app.get("/")
def home(current_user: str = Depends(get_current_user)):
    return {"project": "Vehicle AI Platform",
    "status": "Running",
    "developer": "Nikhil"}


@app.get("/incidents",response_model=list[VehicleIncidentDBModel])
def get_incidents_route(current_user: str = Depends(get_current_user)):
    return get_incidents_service()



@app.post("/incident")
def create_incident_route(data: VehicleIncidentRequestModel, current_user: str = Depends(get_current_user)):
    return create_incident_service(data.model_dump())
  


@app.get("/incident/{id}", response_model=VehicleIncidentDBModel)
def get_incident_by_id_route(id: int, current_user: str = Depends(get_current_user)):
    return get_incident_by_id_service(id)
   


@app.patch("/update_incident/{id}")
def update_incident_id_route(id: int, data: VehicleIncidentUpdateModel, current_user: str = Depends(get_current_user)):
    return update_incident_id_service(id, data.model_dump())


@app.delete("/delete_incident/{id}")
def delete_incident_route(id: int, current_user: str = Depends(get_current_user)):
    return delete_incident_id_service(id)

@app.post("/semantic_search")
def semantic_search_route(query: str, current_user: str = Depends(get_current_user)):
    return search_query(query)

@app.post("/create_user")
def create_user_route(user: UserModel):
    return create_user_service(user)

@app.get("/users")
def get_users_route(current_user: str = Depends(get_current_user)):
    return get_users_service()

@app.post("/login")
def login_route(user: UserModel):
    return login_user_service(user)
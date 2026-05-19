from fastapi import FastAPI
from Models.VehicleIncidentModel import *
from Services.Incidents import *
from DatabaseLayer.db import init_db

init_db()  # Initialize the database when the application starts

app = FastAPI() 

@app.get("/")
def home():
    return {"project": "Vehicle AI Platform",
    "status": "Running",
    "developer": "Nikhil"}

@app.get("/incidents",response_model=list[VehicleIncidentDBModel])
def get_incidents_route():
    return get_incidents_service()

@app.post("/incident")
def create_incident_route(data: VehicleIncidentRequestModel):
    return create_incident_service(data.model_dump())

@app.get("/incident/{id}", response_model=VehicleIncidentDBModel)
def get_incident_by_id_route(id: int):
    return get_incident_by_id_service(id)

@app.post("/update_incident/{id}")
def update_incident_id_route(id: int, data: VehicleIncidentUpdateModel):
    return update_incident_id_service(id, data.model_dump())

@app.delete("/delete_incident/{id}")
def delete_incident_route(id: int):
    return delete_incident_id_service(id)


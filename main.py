from fastapi import FastAPI, HTTPException
from Models.VehicleIncidentModel import *
from Services.Incidents import *
from DatabaseLayer.db import init_db
from Services.Exceptions.IncidentExceptions import *

init_db()  # Initialize the database when the application starts

app = FastAPI() 

@app.get("/")
def home():
    return {"project": "Vehicle AI Platform",
    "status": "Running",
    "developer": "Nikhil"}

@app.get("/incidents",response_model=list[VehicleIncidentDBModel])
def get_incidents_route():
    try:
        return get_incidents_service()
    except IncidentRetrievalError as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.post("/incident")
def create_incident_route(data: VehicleIncidentRequestModel):
    try:
        return create_incident_service(data.model_dump())
    except IncidentCreationError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/incident/{id}", response_model=VehicleIncidentDBModel)
def get_incident_by_id_route(id: int):
    try:
        return get_incident_by_id_service(id)
    except IncidentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except IncidentRetrievalError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/update_incident/{id}")
def update_incident_id_route(id: int, data: VehicleIncidentUpdateModel):
    try:
        return update_incident_id_service(id, data.model_dump())
    except IncidentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except IncidentUpdateError as e:
        raise HTTPException(status_code=400, detail=str(e))
   

@app.delete("/delete_incident/{id}")
def delete_incident_route(id: int):
    try:
        return delete_incident_id_service(id)
    except IncidentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except IncidentDeletionError as e:
        raise HTTPException(status_code=400, detail=str(e))


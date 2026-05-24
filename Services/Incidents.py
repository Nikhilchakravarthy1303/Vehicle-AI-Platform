from AIIntelligenceWorkflows.Exceptions.IncidentAIExceptions import *
from Models.VehicleIncidentModel import *
from DatabaseLayer.db import get_incidents_db, create_incident_db, get_incident_by_id_db, update_incident_id_db, delete_incident_id_db
from Services.Exceptions.IncidentExceptions import *
from AIIntelligenceWorkflows.IncidentAIWorkflow import process_incident_intelligence
from AIIntelligenceWorkflows.IncidentIntelligenceRetrievalWorkflow import retrieve_incidents_intelligence

def get_incidents_service():
    try:
        return get_incidents_db()
    except Exception as e:
        raise IncidentRetrievalError(f"Error fetching incidents") from e


def create_incident_service(data):
    try:
        return process_incident_intelligence(data)
    except Exception as e:
        raise IncidentCreationError(f"Error creating incident") from e



def get_incident_by_id_service(id):
    try:
        incidents = get_incident_by_id_db(id)
        if incidents:
            return incidents[0]
        else:
            raise IncidentNotFoundError(f"Incident with id {id} not found")
    except IncidentNotFoundError:
        raise
    except IncidentRetrievalError as e:
        raise IncidentRetrievalError(f"Error fetching incident by ID") from e



def update_incident_id_service(id, data):
    # This function would contain logic to update the incident in the database
    # For now, it's a placeholder to show where the update logic would go
    try:
        incidents = get_incident_by_id_db(id)
        if not incidents:
            raise IncidentNotFoundError(f"Incident with id {id} not found")
        update_incident_id_db(id, data)
        return {"message": "Incident updated successfully"}
    except IncidentNotFoundError:
        raise
    except IncidentUpdateError as e:
        raise IncidentUpdateError(f"Error updating incident") from e



def delete_incident_id_service(id):
    # This function would contain logic to delete the incident from the database
    # For now, it's a placeholder to show where the delete logic would go
    try:
        incidents = get_incident_by_id_db(id)
        if not incidents:
            raise IncidentNotFoundError(f"Incident with id {id} not found")
        delete_incident_id_db(id)
        return {"message": "Incident deleted successfully"}
    except IncidentNotFoundError:
        raise   
    except IncidentDeletionError as e:
        raise IncidentDeletionError(f"Error deleting incident") from e
    

def search_query(query):
    try:
        return retrieve_incidents_intelligence(query)
    except Exception as e:
        raise IncidentRetrievalError(f"Error retrieving results for query: {query}") from e
    



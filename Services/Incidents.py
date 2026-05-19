from Models.VehicleIncidentModel import *
from DatabaseLayer.db import get_incidents_db, create_incident_db, get_incident_by_id_db, update_incident_id_db, delete_incident_id_db

def get_incidents_service():
    return get_incidents_db()

def create_incident_service(data):
    if "engine" in data["issue"].lower():
        create_incident_db({
            "vehicle": data["vehicle"],
            "issue": data["issue"],
            "category": "engine",
            "status": "high",
            "action": "Inspect immediately"
        })
        return VehicleIncidentResponseModel(category="engine", status="high", action="Inspect immediately")
    elif "brake" in data["issue"].lower():
        create_incident_db({
            "vehicle": data["vehicle"],
            "issue": data["issue"],
            "category": "brake",
            "status": "critical",
            "action": "Inspect immediately"
        })
        return VehicleIncidentResponseModel(category="brake", status="critical", action="Inspect immediately")
    elif "battery" in data["issue"].lower():
        create_incident_db({
            "vehicle": data["vehicle"],
            "issue": data["issue"],
            "category": "battery",
            "status": "medium",
            "action": "Schedule maintenance"
        })
        return VehicleIncidentResponseModel(category="battery", status="medium", action="Schedule maintenance")
    else:
        create_incident_db({
            "vehicle": data["vehicle"],
            "issue": data["issue"],
            "category": "general",
            "status": "normal",
            "action": "Monitor vehicle"
        })
        return VehicleIncidentResponseModel(category="general", status="normal", action="Monitor vehicle")
    
def get_incident_by_id_service(id):
    incidents = get_incident_by_id_db(id)
    if incidents:
        return incidents[0]
    else:
        return None
    
def update_incident_id_service(id, data):
    # This function would contain logic to update the incident in the database
    # For now, it's a placeholder to show where the update logic would go
    return update_incident_id_db(id, data)

def delete_incident_id_service(id):
    # This function would contain logic to delete the incident from the database
    # For now, it's a placeholder to show where the delete logic would go
    return delete_incident_id_db(id)
from AIIntelligenceWorkflows.Exceptions.IncidentAIExceptions import *
from Models.VehicleIncidentModel import *
from DatabaseLayer.db import get_incidents_db, create_incident_db, get_incident_by_id_db, get_user_by_username_db, get_users_db, update_incident_id_db, delete_incident_id_db, create_user_db
from Services.Exceptions.IncidentExceptions import *
from AIIntelligenceWorkflows.IncidentAIWorkflow import process_incident_intelligence
from AIIntelligenceWorkflows.IncidentIntelligenceRetrievalWorkflow import retrieve_incidents_intelligence
from Models.UserModel import UserModel
from AuthHandler.PasswordHandler import *
from AuthHandler.JWTHandler import *


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
    


def create_user_service(user: UserModel):
    try:
        hashed_password = hash_password(user.password)
        # Here you would add logic to save the user to the database
        # For now, it's a placeholder to show where the user creation logic would go
        user_id = create_user_db(user.username, hashed_password,"USER")
        return {"message": f"User {user.username} created successfully", "user_id": user_id}
    except Exception as e:
        raise UserCreationError(f"Error creating user: {user.username}") from e




def get_users_service():
    try:
        return get_users_db()
    except Exception as e:
        raise UserRetrievalError(f"Error fetching users") from e
    


def login_user_service(user: UserModel):
    try:
        user_record = get_user_by_username_db(user.username)
        if not user_record:
            raise UserRetrievalError(f"User {user.username} not found")
        stored_hashed_password = user_record[0]["hashed_password"]  # Assuming the hashed password is in the third column
        if verify_password(user.password, stored_hashed_password):
            access_token = create_access_token(data={"sub": user.username})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise AuthenticationError(f"Invalid credentials for user {user.username}")
    except UserRetrievalError:
        raise
    except AuthenticationError:
        raise
    except Exception as e:
        raise UserRetrievalError(f"Error during login for user: {user.username}") from e
        
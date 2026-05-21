from Services.Exceptions.IncidentExceptions import *

def register_exception_handlers(app):
    from ExceptionHandlers.Services.IncidentHandler import (
        incident_not_found_handler,
        incident_retrieval_handler,
        incident_creation_handler,
        incident_update_handler,
        incident_deletion_handler,
    )
    
    app.add_exception_handler(IncidentNotFoundError, incident_not_found_handler)
    app.add_exception_handler(IncidentRetrievalError, incident_retrieval_handler)
    app.add_exception_handler(IncidentCreationError, incident_creation_handler)
    app.add_exception_handler(IncidentUpdateError, incident_update_handler)
    app.add_exception_handler(IncidentDeletionError, incident_deletion_handler)
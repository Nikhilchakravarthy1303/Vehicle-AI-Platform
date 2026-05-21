from fastapi import Request
from Services.Incidents import *
from fastapi.responses import JSONResponse


async def incident_not_found_handler(request: Request, exc: IncidentNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )

async def incident_retrieval_handler(request: Request, exc: IncidentRetrievalError):
    return JSONResponse(
        status_code=503,
        content={"message": str(exc)},
    )

async def incident_creation_handler(request: Request, exc: IncidentCreationError):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )

async def incident_update_handler(request: Request, exc: IncidentUpdateError):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )

async def incident_deletion_handler(request: Request, exc: IncidentDeletionError):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )


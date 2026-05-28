from fastapi import Request
from fastapi.responses import JSONResponse

from Services.Incidents import *

from Core.Logging import setup_logging


logger = setup_logging()


async def incident_not_found_handler(
    request: Request,
    exc: IncidentNotFoundError
):

    logger.warning(
        f"""
        Incident not found |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc)
        }
    )


async def incident_retrieval_handler(
    request: Request,
    exc: IncidentRetrievalError
):

    logger.exception(
        f"""
        Incident retrieval failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=503,
        content={
            "message": str(exc)
        }
    )


async def incident_creation_handler(
    request: Request,
    exc: IncidentCreationError
):

    logger.exception(
        f"""
        Incident creation failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=500,
        content={
            "message": str(exc)
        }
    )


async def incident_update_handler(
    request: Request,
    exc: IncidentUpdateError
):

    logger.exception(
        f"""
        Incident update failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=500,
        content={
            "message": str(exc)
        }
    )


async def incident_deletion_handler(
    request: Request,
    exc: IncidentDeletionError
):

    logger.exception(
        f"""
        Incident deletion failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=500,
        content={
            "message": str(exc)
        }
    )

async def user_creation_handler(
    request: Request,
    exc: UserCreationError
):

    logger.exception(
        f"""
        User creation failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=500,
        content={
            "message": str(exc)
        }
    )


async def user_retrieval_handler(
    request: Request,
    exc: UserRetrievalError
):

    logger.exception(
        f"""
        User retrieval failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=503,
        content={
            "message": str(exc)
        }
    )

async def authentication_error_handler(
    request: Request,
    exc: AuthenticationError
):

    logger.warning(
        f"""
        Authentication failed |
        method={request.method} |
        path={request.url.path} |
        detail={exc}
        """
    )

    return JSONResponse(
        status_code=401,
        content={
            "message": str(exc)
        }
    )
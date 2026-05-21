class IncidentError(Exception):
    pass


class IncidentRetrievalError(IncidentError):
    pass


class IncidentCreationError(IncidentError):
    pass


class IncidentUpdateError(IncidentError):
    pass


class IncidentDeletionError(IncidentError):
    pass


class IncidentNotFoundError(IncidentError):
    pass
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

class UserCreationError(Exception):
    pass

class UserRetrievalError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class AuthenticationError(Exception):
    pass
class IncidentAIError(Exception):
    """Base class for exceptions in the Incident AI module."""
    pass


class IncidentProcessingError(IncidentAIError):
    """Custom exception for errors during incident summarization."""
    pass


from AIIntelligenceWorkflows.Exceptions.IncidentAIExceptions import *
from VectorDB.ChromaClient import search_incidents_in_chroma


def retrieve_incidents_intelligence(query):
    try:
        results = search_incidents_in_chroma(query)
        return {"results": results, "query": query}
    except Exception as e:
        raise IncidentIntelligenceRetrievalError(f"Error performing semantic search") from e
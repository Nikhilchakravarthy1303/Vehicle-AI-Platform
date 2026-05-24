from AIIntelligenceWorkflows.Exceptions.IncidentAIExceptions import *
from VectorDB.ChromaClient import search_incidents_in_chroma

VALID_SEVERITIES = {
    "low": "LOW",
    "medium": "MEDIUM",
    "high": "HIGH",
    "critical": "CRITICAL"
}

VALID_STATUSES = {
    "open": "OPEN",
    "resolved": "RESOLVED",
    "in progress": "IN_PROGRESS"
}

def parse_query(query):

    filters = {}

    semantic_query = query.lower()

    for severity_word, severity_value in VALID_SEVERITIES.items():

        if severity_word in semantic_query:

            filters["severity"] = severity_value

            semantic_query = semantic_query.replace(
                severity_word,
                ""
            )

    for status_word, status_value in VALID_STATUSES.items():

        if status_word in semantic_query:

            filters["status"] = status_value

            semantic_query = semantic_query.replace(
                status_word,
                ""
            )

    semantic_query = semantic_query.strip()

    return semantic_query, filters

def retrieve_incidents_intelligence(query):
    try:
        parser_query, filters = parse_query(query)
        results = search_incidents_in_chroma(parser_query, filters)

        filtered_results = []

        for index, distance in enumerate(results["distances"][0]):

            if distance < 1.5:

                filtered_results.append({
                    "id": results["ids"][0][index],
                    "metadata": results["metadatas"][0][index],
                    "document": results["documents"][0][index],
                    "distance": distance
                })

        if not filtered_results:
            return {
                "query": query,
                "results": [],
                "message": "No relevant incidents found for the query."
            }
        return {
            "query": query,
            "results": filtered_results
        }

    except Exception as e:
        raise IncidentIntelligenceRetrievalError(
            "Error performing semantic search"
        ) from e
from AIIntelligenceWorkflows.Exceptions.IncidentAIExceptions import *
from openai import OpenAI
import os
import json
from VectorDB.ChromaClient import add_incident_to_chroma 
from DatabaseLayer.db import create_incident_db

valid_severities = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

def process_incident_intelligence(incident_description):
    try:
        client = OpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """
                        You are an AI assistant for a vehicle incident management platform.

                        Analyze the vehicle incident and return ONLY valid JSON.

                        Severity MUST be exactly one of:
                        - LOW
                        - MEDIUM
                        - HIGH
                        - CRITICAL

                        Return format:

                        {
                        "summary": "...",
                        "category": "...",
                        "severity": "LOW | MEDIUM | HIGH | CRITICAL",
                        "recommended_action": "..."
                        }
                        """
                },
                {
                    "role": "user",
                    "content": f"Summarize the following incident description: {incident_description}"
                }
            ],
            max_tokens=100,
            temperature=0.5
        )
        content = response.choices[0].message.content

        if not content or content.strip() == "":
            raise IncidentProcessingError(
                "Empty response"
            )
        
        parsed_response = json.loads(content)
        
        if parsed_response == "":
            raise IncidentProcessingError("Empty response")
        if parsed_response["severity"] not in valid_severities:
            raise IncidentProcessingError("Invalid severity level detected")
        
        document = f"Incident: {incident_description}\nSummary: {parsed_response['summary']}\nCategory: {parsed_response['category']}\nSeverity: {parsed_response['severity']}\nRecommended Action: {parsed_response['recommended_action']}\nStatus: OPEN"
        incident_id = create_incident_db({
            "vehicle": incident_description["vehicle"],
            "issue": incident_description["issue"],
            "category": parsed_response["category"],
            "severity": parsed_response["severity"],
            "status": "OPEN",
            "action": parsed_response["recommended_action"]
        })
        add_incident_to_chroma(incident_id=incident_id, description=document, incident={"vehicle": incident_description["vehicle"], "issue": incident_description["issue"], "category": parsed_response["category"], "severity": parsed_response["severity"]})
        return parsed_response
    except Exception as e:
        raise IncidentProcessingError("Error processing incident") from e
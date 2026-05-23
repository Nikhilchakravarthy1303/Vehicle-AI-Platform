from AIInferenceWorkflows.Exceptions.IncidentAIExceptions import *
from openai import OpenAI
import os

def summarize_incident(incident_description):
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
                    "content": "You are an assistant that summarizes vehicle incident descriptions into concise summaries."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following incident description: {incident_description}"
                }
            ],
            max_tokens=100,
            temperature=0.5
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        raise IncidentSummarizationError("Error summarizing incident") from e
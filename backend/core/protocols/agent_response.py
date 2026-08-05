"""
AIS Agent Response Contract (ARC)

Every AIS agent must return responses using this structure.
"""


def create_agent_response(agent_name):

    return {

        "agent": agent_name,

        "status": "completed",

        "confidence": 0,

        "analysis_status": "Pending",

        "proposed_updates": {},

        "recommendations": [],

        "questions": [],

        "requires_more_information": False,

        "next_agent": None,

        "errors": []
    }
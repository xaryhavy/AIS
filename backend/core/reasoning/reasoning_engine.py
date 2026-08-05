"""
AIS Reasoning Engine

Coordinates all reasoning modules.
"""

from core.reasoning.classifier import classify_problem


def analyze(business_context):

    reasoning_result = {}

    classification = classify_problem(business_context)

    reasoning_result["classification"] = classification

    return reasoning_result
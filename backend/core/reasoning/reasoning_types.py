"""
AIS Core
Reasoning Types

Defines the controlled vocabulary used by
the AIS Reasoning Engine.

Using an Enum prevents spelling mistakes,
improves consistency, and standardizes
reasoning across all AIS modules.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from enum import Enum


class ReasoningType(Enum):
    """
    Standard reasoning categories used throughout AIS.
    """

    OBSERVATION = "Observation"

    EVIDENCE = "Evidence"

    INFERENCE = "Inference"

    VALIDATION = "Validation"

    DECISION = "Decision"

    RECOMMENDATION = "Recommendation"

    LEARNING = "Learning"

    WARNING = "Warning"

    ERROR = "Error"
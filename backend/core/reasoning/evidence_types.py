"""
AIS Core
Evidence Types

Defines the standard categories of evidence used
throughout the AIS reasoning system.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from enum import Enum


class EvidenceType(Enum):
    """
    Standard evidence categories.
    """

    KEYWORD = "Keyword"

    FACT = "Fact"

    OBSERVATION = "Observation"

    METRIC = "Metric"

    PATTERN = "Pattern"

    TREND = "Trend"

    BUSINESS_CONTEXT = "Business Context"

    BUSINESS_MEMORY = "Business Memory"

    EXTERNAL_DATA = "External Data"

    LLM = "LLM"

    USER_INPUT = "User Input"
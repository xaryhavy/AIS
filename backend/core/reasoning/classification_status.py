"""
AIS Core
Classification Status

Represents the outcome of a classification process.

Status answers:
"What happened?"

ProblemCategory answers:
"What problem was identified?"

Author: Fabian Ezenwajiaku
Project: AIS
"""

from enum import Enum


class ClassificationStatus(Enum):
    """
    Status of a completed classification.
    """

    SUCCESS = "Success"

    INSUFFICIENT_EVIDENCE = "Insufficient Evidence"

    CONFLICTING_EVIDENCE = "Conflicting Evidence"

    LOW_CONFIDENCE = "Low Confidence"

    FAILED = "Failed"
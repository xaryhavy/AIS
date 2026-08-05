"""
AIS Core
Classification Result

Represents the outcome of a classification.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from dataclasses import dataclass, field

from core.reasoning.problem_categories import ProblemCategory
from core.reasoning.classification_status import ClassificationStatus
from core.reasoning.evidence import Evidence


@dataclass(slots=True)
class ClassificationResult:
    """
    Represents the output of the classifier.
    """

    status: ClassificationStatus

    category: ProblemCategory

    confidence: float

    supporting_evidence: list[Evidence] = field(default_factory=list)

    conflicting_evidence: list[Evidence] = field(default_factory=list)

    missing_information: list[str] = field(default_factory=list)

    matched_patterns: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    def is_successful(self) -> bool:

        return self.status == ClassificationStatus.SUCCESS

    def is_confident(self, threshold: float = 0.75) -> bool:

        return self.confidence >= threshold

    def evidence_count(self) -> int:

        return len(self.supporting_evidence)

    def conflict_count(self) -> int:

        return len(self.conflicting_evidence)

    def to_dict(self):

        return {

            "status": self.status.value,

            "category": self.category.value,

            "confidence": self.confidence,

            "supporting_evidence": [

                evidence.to_dict()

                for evidence in self.supporting_evidence

            ],

            "conflicting_evidence": [

                evidence.to_dict()

                for evidence in self.conflicting_evidence

            ],

            "missing_information": self.missing_information,

            "matched_patterns": self.matched_patterns,

            "metadata": self.metadata

        }

    def __str__(self):

        return (

            f"{self.status.value}"

            f" | "

            f"{self.category.value}"

            f" | "

            f"{self.confidence:.2f}"

        )
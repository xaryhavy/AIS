"""
AIS Core
Evidence

Represents one structured piece of evidence
used during reasoning.

Evidence always exists before reasoning.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from core.reasoning.evidence_types import EvidenceType


@dataclass(slots=True)
class Evidence:
    """
    Represents one piece of structured evidence.
    """

    source: str

    evidence_type: EvidenceType

    value: str

    confidence: float = 1.0

    importance: float = 1.0

    metadata: dict = field(default_factory=dict)

    evidence_id: str = field(
        default_factory=lambda: f"EVID-{uuid4().hex[:8].upper()}"
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self):

        return {

            "evidence_id": self.evidence_id,

            "source": self.source,

            "evidence_type": self.evidence_type.value,

            "value": self.value,

            "confidence": self.confidence,

            "importance": self.importance,

            "metadata": self.metadata,

            "created_at": self.created_at

        }

    def __str__(self):

        return (

            f"{self.evidence_type.value}"

            f" | "

            f"{self.value}"

            f" | "

            f"{self.source}"

        )
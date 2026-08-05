"""
AIS Core
Reasoning Atom

The smallest unit of reasoning inside AIS.

Every thought produced by AIS is represented
as a Reasoning Atom.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from core.reasoning.reasoning_types import ReasoningType


@dataclass(slots=True)
class ReasoningAtom:
    """
    Represents one reasoning event inside AIS.
    """

    step: int

    module: str

    reasoning_type: ReasoningType

    reason: str

    confidence: float | None = None

    metadata: dict = field(default_factory=dict)

    atom_id: str = field(
        default_factory=lambda: f"ATOM-{uuid4().hex[:8].upper()}"
    )

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self):

        return {

            "atom_id": self.atom_id,

            "step": self.step,

            "module": self.module,

            "reasoning_type": self.reasoning_type.value,

            "reason": self.reason,

            "confidence": self.confidence,

            "metadata": self.metadata,

            "created_at": self.created_at

        }

    def __str__(self):

        return (

            f"[{self.step}] "

            f"{self.module} "

            f"({self.reasoning_type.value}) "

            f"- {self.reason}"

        )
"""
AIS Core
Reasoning Trace

Records every reasoning event produced during
a single AIS reasoning cycle.

The trace acts as the journal of thought for AIS.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from core.reasoning.reasoning_atom import ReasoningAtom
from core.reasoning.reasoning_types import ReasoningType


@dataclass(slots=True)
class ReasoningTrace:
    """
    Stores every reasoning atom generated during
    one AIS reasoning session.
    """

    ais_version: str = "0.1.0"

    trace_uuid: str = field(
        default_factory=lambda: str(uuid4())
    )

    display_id: str = field(
        default_factory=lambda:
        f"AIS-TRACE-{uuid4().hex[:8].upper()}"
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    atoms: list[ReasoningAtom] = field(default_factory=list)

    def record(
        self,
        module: str,
        reasoning_type: ReasoningType,
        reason: str,
        confidence: float | None = None,
        metadata: dict | None = None,
    ) -> ReasoningAtom:
        """
        Records one reasoning event.
        """

        atom = ReasoningAtom(
            step=len(self.atoms) + 1,
            module=module,
            reasoning_type=reasoning_type,
            reason=reason,
            confidence=confidence,
            metadata=metadata or {}
        )

        self.atoms.append(atom)

        return atom

    def latest(self) -> ReasoningAtom | None:
        """
        Returns the latest reasoning atom.
        """

        if not self.atoms:
            return None

        return self.atoms[-1]

    def get_atoms(self) -> list[dict]:
        """
        Returns all reasoning atoms as dictionaries.
        """

        return [

            atom.to_dict()

            for atom in self.atoms

        ]

    def total_steps(self) -> int:
        """
        Returns the total number of reasoning steps.
        """

        return len(self.atoms)

    def participating_modules(self) -> list[str]:
        """
        Returns the modules that participated
        in this reasoning cycle.
        """

        return sorted({

            atom.module

            for atom in self.atoms

        })

    def reasoning_path(self) -> list[str]:
        """
        Returns the sequence of reasoning
        types followed during this reasoning cycle.
        """

        return [

            atom.reasoning_type.value

            for atom in self.atoms

        ]

    def summary(self) -> dict:
        """
        Returns a high-level summary of the trace.
        """

        return {

            "display_id": self.display_id,

            "total_steps": self.total_steps(),

            "participating_modules": self.participating_modules(),

            "reasoning_path": self.reasoning_path()

        }

    def export(self) -> dict:
        """
        Exports the complete reasoning trace.
        """

        return {

            "trace_uuid": self.trace_uuid,

            "display_id": self.display_id,

            "created_at": self.created_at,

            "ais_version": self.ais_version,

            "summary": self.summary(),

            "atoms": self.get_atoms()

        }

    def clear(self) -> None:
        """
        Clears the reasoning trace.
        """

        self.atoms.clear()

    def __len__(self) -> int:

        return len(self.atoms)

    def __str__(self) -> str:

        return (

            f"{self.display_id}"

            f" | "

            f"{self.total_steps()} reasoning steps"

        )
"""Illustrative edition lifecycle; not a production authorization control."""
from dataclasses import dataclass, replace
from enum import Enum


class EditionState(str, Enum):
    DRAFT = "draft"
    RESEARCHED = "researched"
    EDITED = "edited"
    READY_FOR_REVIEW = "ready_for_review"
    APPROVED = "approved"
    DELIVERED = "delivered"


_ALLOWED = {
    EditionState.DRAFT: {EditionState.RESEARCHED},
    EditionState.RESEARCHED: {EditionState.EDITED},
    EditionState.EDITED: {EditionState.READY_FOR_REVIEW},
    EditionState.READY_FOR_REVIEW: {EditionState.EDITED, EditionState.APPROVED},
    EditionState.APPROVED: {EditionState.EDITED, EditionState.DELIVERED},
    EditionState.DELIVERED: set(),
}


@dataclass(frozen=True)
class Edition:
    identifier: str
    state: EditionState = EditionState.DRAFT

    def advance(self, target: EditionState) -> "Edition":
        if target not in _ALLOWED[self.state]:
            raise ValueError(f"Invalid transition: {self.state.value} -> {target.value}")
        return replace(self, state=target)

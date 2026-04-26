from dataclasses import dataclass, field
from typing import List
from .Session import Session


@dataclass
class Sessions:
    available: bool = None
    metadata: List[Session] = field(default_factory=list)

    @classmethod
    def from_dict(cls, item: dict) -> "Sessions":
        if item is None:
            return None
        return cls(
            available=item.get("available"),
            metadata=[
                Session.from_dict(s)
                for s in (item.get("metadata") or [])
            ],
        )

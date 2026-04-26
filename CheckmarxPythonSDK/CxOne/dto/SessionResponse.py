from dataclasses import dataclass


@dataclass
class SessionResponse:
    id: str = None
    status: str = None
    scan_id: str = None

    @classmethod
    def from_dict(cls, item: dict) -> "SessionResponse":
        if item is None:
            return None
        return cls(
            id=item.get("id"),
            status=item.get("status"),
            scan_id=item.get("scanId"),
        )

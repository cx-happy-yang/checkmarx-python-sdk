from dataclasses import dataclass


@dataclass
class AsyncRequestResponse:
    id: str = None

    def to_dict(self):
        return {"id": self.id}

    @classmethod
    def from_dict(cls, item: dict) -> "AsyncRequestResponse":
        return cls(id=item.get("id"))

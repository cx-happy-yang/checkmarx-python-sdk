from dataclasses import dataclass


@dataclass
class SastStatus:
    ready: bool = None
    message: str = None


    @classmethod
    def from_dict(cls, item: dict) -> "SastStatus":
        if item is None:
            return None
        return cls(ready=item.get("ready"), message=item.get("message"))

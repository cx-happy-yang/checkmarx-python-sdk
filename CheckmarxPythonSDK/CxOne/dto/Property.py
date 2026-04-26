from dataclasses import dataclass


@dataclass
class Property:
    key: str = None
    value: str = None

    @classmethod
    def from_dict(cls, item: dict) -> "Property":
        if item is None:
            return None
        return cls(key=item.get("key"), value=item.get("value"))

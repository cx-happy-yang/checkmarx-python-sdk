from dataclasses import dataclass


@dataclass
class MethodParameter:
    """

    Args:
        name (str):
        label (str):
        documentation (str):
    """

    name: str
    label: str
    documentation: str


    @classmethod
    def from_dict(cls, item: dict) -> "MethodParameter":
        if item is None:
            return None
        return cls(
            name=item.get("name"),
            label=item.get("label"),
            documentation=item.get("documentation"),
        )

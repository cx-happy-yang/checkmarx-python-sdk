from dataclasses import dataclass


@dataclass
class Metadata:
    cwe: int
    severity: int
    is_executable: bool
    cx_description_id: int

    @classmethod
    def from_dict(cls, item: dict) -> "Metadata":
        return cls(
            cwe=item.get("Cwe"),
            severity=item.get("Severity"),
            is_executable=item.get("IsExecutable"),
            cx_description_id=item.get("CxDescriptionID"),
        )

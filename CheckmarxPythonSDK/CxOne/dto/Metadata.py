from dataclasses import dataclass


@dataclass
class Metadata:
    cwe: int
    severity: int
    is_executable: bool
    cx_description_id: int

    def to_dict(self):
        return {
            "Cwe": self.cwe,
            "Severity": self.severity,
            "IsExecutable": self.is_executable,
            "CxDescriptionID": self.cx_description_id,
        }

    @classmethod
    def from_dict(cls, item: dict) -> "Metadata":
        if item is None:
            return None
        return cls(
            cwe=item.get("Cwe"),
            severity=item.get("Severity"),
            is_executable=item.get("IsExecutable"),
            cx_description_id=item.get("CxDescriptionID"),
        )

from dataclasses import dataclass


@dataclass
class TriageResponse:
    result_id: str = None
    project_id: str = None
    state: str = None
    severity: str = None

    def to_dict(self):
        return {
            "resultId": self.result_id,
            "projectId": self.project_id,
            "state": self.state,
            "severity": self.severity,
        }

    @classmethod
    def from_dict(cls, item: dict) -> "TriageResponse":
        return cls(
            result_id=item.get("resultId"),
            project_id=item.get("projectId"),
            state=item.get("state"),
            severity=item.get("severity"),
        )


def construct_triage_response(item):
    return TriageResponse.from_dict(item)

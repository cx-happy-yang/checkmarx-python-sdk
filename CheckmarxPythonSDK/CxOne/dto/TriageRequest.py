from dataclasses import dataclass

@dataclass
class TriageRequest:
    result_id: str = None
    project_id: str = None
    state: str = None
    severity: str = None

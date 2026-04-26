from dataclasses import dataclass


@dataclass
class SessionRequest:
    project_id: str
    scan_id: str
    scanner: str = "sast"
    timeout: int = None
    upload_url: str = None

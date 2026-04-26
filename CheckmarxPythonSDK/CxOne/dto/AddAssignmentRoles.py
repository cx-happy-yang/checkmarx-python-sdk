from dataclasses import dataclass
from typing import List

@dataclass
class AddAssignmentRoles:
    entity_id: str = None
    resource_id: str = None
    entity_roles: List[str] = None

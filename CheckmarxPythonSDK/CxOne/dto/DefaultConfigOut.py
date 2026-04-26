from dataclasses import dataclass


@dataclass
class DefaultConfigOut:
    id: str = None
    name: str = None
    description: str = None
    url: str = None
    is_tenant_default: bool = None
    associated_projects: int = None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "isTenantDefault": self.is_tenant_default,
            "associatedProjects": self.associated_projects,
        }

    @classmethod
    def from_dict(cls, item: dict) -> "DefaultConfigOut":
        if item is None:
            return None
        return cls(
            id=item.get("id"),
            name=item.get("name"),
            description=item.get("description"),
            url=item.get("url"),
            is_tenant_default=item.get("isTenantDefault"),
            associated_projects=item.get("associatedProjects"),
        )

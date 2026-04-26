from dataclasses import dataclass
from typing import List


@dataclass
class Project:
    id: str = None
    name: str = None
    groups: List[str] = None
    repo_url: str = None
    main_branch: str = None
    origin: str = None
    repo_id: int = None
    created_at: str = None
    updated_at: str = None
    tags: dict = None
    criticality: int = 3

    def to_dict(self):
        data = {}
        if self.id:
            data.update({"id": self.id})
        if self.tags:
            data.update({"tags": self.tags})
        return data

    @classmethod
    def from_dict(cls, item: dict) -> "Project":
        return cls(
            id=item.get("id"),
            name=item.get("name"),
            groups=item.get("groups"),
            repo_url=item.get("repoUrl"),
            main_branch=item.get("mainBranch"),
            origin=item.get("origin"),
            repo_id=item.get("repoId"),
            created_at=item.get("createdAt"),
            updated_at=item.get("updatedAt"),
            tags=item.get("tags"),
            criticality=item.get("criticality"),
        )


def construct_project(item):
    return Project.from_dict(item)

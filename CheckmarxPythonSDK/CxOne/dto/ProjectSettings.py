from dataclasses import dataclass
from .Scanner import Scanner
from typing import List


@dataclass
class ProjectSettings:
    """

    Args:
        web_hook_enabled (bool): If true, a webhook is enabled for each repo.
        decorate_pull_requests (bool): If true, pull request decorations will be sent to the repo.
                        Note: This requires webhookEnabled to be set as true.
        is_private_package (bool): If true the project will be marked as a private package for SCA scans. (Not
            currently supported)
        scanners (list of Scanner):
        tags (dict):
        groups (list of str):
    """

    web_hook_enabled: bool = None
    decorate_pull_requests: bool = None
    is_private_package: bool = None
    scanners: List[Scanner] = None
    tags: dict = None
    groups: List[str] = None

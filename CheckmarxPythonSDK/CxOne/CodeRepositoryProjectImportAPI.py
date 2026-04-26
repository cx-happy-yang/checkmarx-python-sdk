from CheckmarxPythonSDK.api_client import ApiClient
from CheckmarxPythonSDK.CxOne.config import construct_configuration
from .dto import SCMImportInput


class CodeRepositoryProjectImportAPI(object):

    def __init__(self, api_client: ApiClient = None):
        if api_client is None:
            configuration = construct_configuration()
            api_client = ApiClient(configuration=configuration)
        self.api_client = api_client
        self.base_url = (
            f"{self.api_client.configuration.server_base_url}/api/repos-manager"
        )

    def import_code_repository(self, scm_import_input: SCMImportInput) -> dict:
        """
        Args:
            scm_import_input (SCMImportInput):

        Returns:
            dict with keys:
                processId (str): The unique identifier of the conversion process.
                message (str): A message including the URL for checking the
                    conversion status.
        """
        url = f"{self.base_url}/scm-projects"
        response = self.api_client.call_api(
            method="POST", url=url, json={
                "scm": {"type": scm_import_input.scm.type, "token": scm_import_input.scm.token},
                "organization": {
                    "orgIdentity": scm_import_input.organization.org_identity,
                    "monitorForNewProjects": scm_import_input.organization.monitor_for_new_projects,
                },
                "defaultProjectSettings": {
                    "decoratePullRequests": scm_import_input.default_project_settings.decorate_pull_requests,
                    "webhookEnabled": scm_import_input.default_project_settings.web_hook_enabled,
                    "scanners": [
                        {
                            "type": s.type,
                            **({"enableAutoPullRequests": s.enable_auto_pull_requests} if s.enable_auto_pull_requests is not None else {}),
                            **({"incrementalScan": s.incremental_scan} if s.incremental_scan is not None else {}),
                        }
                        for s in (scm_import_input.default_project_settings.scanners or [])
                    ],
                    **({"tags": scm_import_input.default_project_settings.tags} if scm_import_input.default_project_settings.tags is not None else {}),
                    **({"groups": scm_import_input.default_project_settings.groups} if scm_import_input.default_project_settings.groups is not None else {}),
                },
                "scanProjectsAfterImport": scm_import_input.scan_projects_after_import,
                "projects": [
                    {
                        "scmRepositoryUrl": p.scm_repository_url,
                        **({"protectedBranches": p.protected_branches} if p.protected_branches is not None else {}),
                        **({"sshKey": p.ssh_key} if p.ssh_key is not None else {}),
                        **({"branchToScanUponCreation": p.branch_to_scan_upon_creation} if p.branch_to_scan_upon_creation is not None else {}),
                        **({"customSettings": {
                            "decoratePullRequests": p.custom_settings.decorate_pull_requests,
                            "webhookEnabled": p.custom_settings.web_hook_enabled,
                            "scanners": [
                                {
                                    "type": s.type,
                                    **({"enableAutoPullRequests": s.enable_auto_pull_requests} if s.enable_auto_pull_requests is not None else {}),
                                    **({"incrementalScan": s.incremental_scan} if s.incremental_scan is not None else {}),
                                }
                                for s in (p.custom_settings.scanners or [])
                            ],
                            **({"tags": p.custom_settings.tags} if p.custom_settings.tags is not None else {}),
                            **({"groups": p.custom_settings.groups} if p.custom_settings.groups is not None else {}),
                        }} if p.custom_settings is not None else {}),
                    }
                    for p in (scm_import_input.projects or [])
                ],
            }
        )
        item = response.json()
        return {
            "processId": item.get("processId"),
            "message": item.get("message"),
        }

    def retrieve_import_status(self, process_id: str) -> dict:
        """
        Args:
            process_id (str): The unique identifier of the import process.

        Returns:
            dict with keys:
                currentPhase (str): Allowed values: PROCESSING_REPOSITORIES,
                    CONFIGURING_REPOSITORIES,
                    CREATING_CHECKMARX_ONE_PROJECTS, DONE
                percentage (int): Percentage of the overall process completed.
                result (dict): Returned only when currentPhase is DONE.
                    status (str): Outcome status: PARTIAL, OK, FAILURE
                    totalProjects (int): Total number of projects attempted.
                    successfulProjectCount (int): Number of successful projects.
                    successfulProjects (list): Successfully created projects.
                    failedProjects (list): Projects that failed to be created.
        """
        url = f"{self.base_url}/scm-projects/import-status"
        params = {"process-id": process_id}
        response = self.api_client.call_api(method="GET", url=url, params=params)
        item = response.json()
        response_data = {
            "currentPhase": item.get("currentPhase"),
            "percentage": item.get("percentage"),
        }
        if "result" in item:
            response_data["result"] = item["result"]
        return response_data


def import_code_repository(scm_import_input: SCMImportInput) -> dict:
    return CodeRepositoryProjectImportAPI().import_code_repository(
        scm_import_input=scm_import_input
    )


def retrieve_import_status(process_id: str) -> dict:
    return CodeRepositoryProjectImportAPI().retrieve_import_status(
        process_id=process_id
    )

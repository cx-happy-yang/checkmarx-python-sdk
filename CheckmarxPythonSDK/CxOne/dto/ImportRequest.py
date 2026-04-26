from dataclasses import dataclass

@dataclass
class ImportRequest:
    """

    Args:
        project_id (str): The id of the project for which the results are being imported
        upload_url (str): The url to upload the file
    """

    project_id: str
    upload_url: str

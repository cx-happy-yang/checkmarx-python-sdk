from dataclasses import dataclass


@dataclass
class StartEnrich:
    """

    Args:
        upload_url (str): URL obtained from the uploads service
    """

    upload_url: str

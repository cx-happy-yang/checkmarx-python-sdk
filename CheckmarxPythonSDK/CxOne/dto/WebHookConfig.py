from dataclasses import dataclass


@dataclass
class WebHookConfig:
    """
    Attributes:
       content_type (str):  Webhooks payload content type
       insecure_ssl (bool): Enable SSL verification
       url (str): Payload URL
       secret (str): Post request attached secret
    """

    content_type: str = None
    insecure_ssl: bool = None
    url: str = None
    secret: str = None

    @classmethod
    def from_dict(cls, item: dict) -> "WebHookConfig":
        return cls(
            content_type=item.get("contentType"),
            insecure_ssl=item.get("insecureSsl"),
            url=item.get("url"),
            secret=item.get("secret"),
        )

from dataclasses import dataclass


@dataclass
class ImportResults:
    """
    Args:
        import_id (str): The id of the new import
    """

    import_id: str

    def to_dict(self):
        return {"importId": self.import_id}

    @classmethod
    def from_dict(cls, item: dict) -> "ImportResults":
        return cls(import_id=item.get("importId"))


def construct_import_results(item):
    return ImportResults.from_dict(item)

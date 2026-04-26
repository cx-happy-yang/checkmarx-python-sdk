from dataclasses import dataclass


@dataclass
class ScanParameter:
    key: str = None
    name: str = None
    category: str = None
    origin_level: str = None
    value: str = None
    value_type: str = None
    value_type_params: str = None
    allow_override: bool = None

    def to_dict(self):
        data = {
            "key": self.key,
            "name": self.name,
            "category": self.category,
            "originLevel": self.origin_level,
            "value": self.value,
            "valueType": self.value_type,
            "allowOverride": self.allow_override,
        }
        if self.value_type == "List":
            data["valueTypeParams"] = self.value_type_params
        return data

    @classmethod
    def from_dict(cls, item: dict) -> "ScanParameter":
        if item is None:
            return None
        return cls(
            key=item.get("key"),
            name=item.get("name"),
            category=item.get("category"),
            origin_level=item.get("originLevel"),
            value=item.get("value"),
            value_type=item.get("valueType"),
            value_type_params=item.get("valueTypeParams"),
            allow_override=item.get("allowOverride"),
        )

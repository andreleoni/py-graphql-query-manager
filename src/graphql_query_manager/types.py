from typing import Any, Dict, List, Union

class Field:
    def __init__(self, name: str, field_type: str, sub_fields: List['Field'] = None):
        self.name = name
        self.field_type = field_type
        self.sub_fields = sub_fields or []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.field_type,
            "sub_fields": [sub_field.to_dict() for sub_field in self.sub_fields]
        }

class QueryType:
    def __init__(self, name: str, fields: List[Field]):
        self.name = name
        self.fields = fields

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "fields": [field.to_dict() for field in self.fields]
        }

class IntrospectionData:
    def __init__(self, query_type: QueryType, types: List[Dict[str, Any]]):
        self.query_type = query_type
        self.types = types

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query_type": self.query_type.to_dict(),
            "types": self.types
        }
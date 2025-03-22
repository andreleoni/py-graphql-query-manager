def validate_json_structure(json_data, expected_structure):
    """Validates the JSON data against the expected structure."""
    if not isinstance(json_data, dict):
        raise ValueError("Invalid JSON data: Expected a dictionary.")
    
    for key, expected_type in expected_structure.items():
        if key not in json_data:
            raise ValueError(f"Missing key: {key}")
        if not isinstance(json_data[key], expected_type):
            raise ValueError(f"Invalid type for key '{key}': Expected {expected_type}, got {type(json_data[key])}")

def format_query_fields(fields):
    """Formats the fields for a GraphQL query."""
    if isinstance(fields, list):
        return " ".join(format_query_fields(field) for field in fields)
    elif isinstance(fields, dict):
        return " ".join(f"{key} {{ {format_query_fields(value)} }}" for key, value in fields.items())
    else:
        return str(fields)

def extract_field_names(fields):
    """Extracts field names from the provided structure."""
    if isinstance(fields, list):
        return [extract_field_names(field) for field in fields]
    elif isinstance(fields, dict):
        return {key: extract_field_names(value) for key, value in fields.items()}
    else:
        return fields

def generate_json_from_introspection(introspection_data):
    """Generates a JSON representation from the introspection data."""
    return {
        "types": introspection_data.get("data", {}).get("__schema", {}).get("types", []),
        "queryType": introspection_data.get("data", {}).get("__schema", {}).get("queryType", {}).get("name", "")
    }
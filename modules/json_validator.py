# modules/json_validator.py
from .graph_schemas import GRAPH_SCHEMAS

def validate_graph_json(json_data):
    """
    Validates the input JSON against the defined schemas.
    
    Args:
        json_data (dict): The JSON data to validate.
        
    Returns:
        dict: { "valid": True/False, "error": "...", "graph_type": "..." }
    """
    if not isinstance(json_data, dict):
        return {"valid": False, "error": "Input must be a JSON object (dict).", "graph_type": None}
    
    graph_type = json_data.get("graph_type")
    if not graph_type:
        return {"valid": False, "error": "Missing 'graph_type' field.", "graph_type": None}
    
    if graph_type not in GRAPH_SCHEMAS:
        return {"valid": False, "error": f"Unsupported graph_type: '{graph_type}'.", "graph_type": graph_type}
    
    schema = GRAPH_SCHEMAS[graph_type]
    required_fields = schema["required_fields"]
    
    # Check required fields
    for field in required_fields:
        if field not in json_data:
            return {"valid": False, "error": f"Missing required field: '{field}'.", "graph_type": graph_type}
            
    # Basic data structure check (simplified)
    # In a real scenario, we would recursively validate types.
    # Here we check if 'data' is a list as expected by most schemas.
    if "data" in json_data and not isinstance(json_data["data"], list):
         return {"valid": False, "error": "'data' field must be a list.", "graph_type": graph_type}

    return {"valid": True, "error": None, "graph_type": graph_type}

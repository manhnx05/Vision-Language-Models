# modules/main_pipeline.py
import json
import os
from .json_validator import validate_graph_json
from .graph_drawer import draw_graph
from .doc_exporter import export_docx

def run_pipeline(json_path):
    """
    Runs the full pipeline: Load JSON -> Validate -> Draw -> Export DOCX.
    
    Args:
        json_path (str): Path to the input JSON file.
        
    Returns:
        dict: Result containing paths and status.
    """
    result = {
        "json": json_path,
        "image_path": None,
        "doc_path": None,
        "status": "failed",
        "error": None
    }
    
    try:
        # 1. Load JSON
        if not os.path.exists(json_path):
            result["error"] = f"File not found: {json_path}"
            return result
            
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                result["error"] = f"Invalid JSON: {str(e)}"
                return result

        # 2. Validate
        validation = validate_graph_json(data)
        if not validation["valid"]:
            result["error"] = f"Validation failed: {validation['error']}"
            return result
            
        # Determine output paths
        base_name = os.path.splitext(os.path.basename(json_path))[0]
        # Assuming run from project root or relative paths handled
        # We'll use absolute paths based on the project structure if possible, 
        # or relative to current working directory.
        # Let's assume standard structure relative to this file's parent's parent.
        
        # Get project root (assuming modules/ is one level deep)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(project_root, "outputs")
        
        image_path = os.path.join(output_dir, "images", f"{base_name}.png")
        doc_path = os.path.join(output_dir, "docs", f"{base_name}.docx")
        
        # 3. Draw Graph
        draw_graph(data, image_path)
        result["image_path"] = image_path
        
        # 4. Export DOCX
        export_docx(image_path, doc_path)
        result["doc_path"] = doc_path
        
        result["status"] = "success"
        return result

    except Exception as e:
        result["error"] = str(e)
        return result

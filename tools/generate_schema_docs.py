# generate_schema_docs.py
import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.graph_schemas import GRAPH_SCHEMAS

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(project_root, "GRAPH_SCHEMAS.md")
    
    content = "# VLM Graph Schemas Reference\n\n"
    content += "Tài liệu này định nghĩa cấu trúc JSON cho từng loại biểu đồ, dùng để train/prompt VLM.\n\n"
    content += "| Graph Type | Description | Required Fields |\n"
    content += "| :--- | :--- | :--- |\n"
    
    # Summary Table
    for graph_type, schema in GRAPH_SCHEMAS.items():
        req_fields = ", ".join(schema["required_fields"])
        content += f"| **{graph_type}** | Biểu đồ {graph_type} | `{req_fields}` |\n"
        
    content += "\n---\n\n"
    content += "## Detailed JSON Templates\n\n"
    
    # Detailed Sections
    for graph_type, schema in GRAPH_SCHEMAS.items():
        content += f"### {graph_type.capitalize()}\n\n"
        content += "**Required Fields:**\n"
        for field in schema["required_fields"]:
            content += f"- `{field}`\n"
            
        content += "\n**Data Structure:**\n"
        content += "```json\n"
        content += json.dumps(schema["data_structure"], indent=2)
        content += "\n```\n"
        
        content += "\n**Example JSON:**\n"
        content += "```json\n"
        content += json.dumps(schema["sample"], indent=2)
        content += "\n```\n\n"
        content += "---\n\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Schema documentation generated at: {output_file}")

if __name__ == "__main__":
    main()

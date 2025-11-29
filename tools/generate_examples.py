# generate_examples.py
import json
import os
import sys

# Add current directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.graph_schemas import GRAPH_SCHEMAS

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(project_root, "examples")
    os.makedirs(examples_dir, exist_ok=True)
    
    print(f"Generating examples in {examples_dir}...")
    
    for graph_type, schema in GRAPH_SCHEMAS.items():
        filename = f"{graph_type}.json"
        filepath = os.path.join(examples_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(schema["sample"], f, indent=2)
        print(f"Created {filename}")

if __name__ == "__main__":
    main()

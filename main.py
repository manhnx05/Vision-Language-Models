# main.py
import os
import glob
from modules.main_pipeline import run_pipeline

def main():
    print("Starting VLM Graph Pipeline Demo...")
    
    # Define paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(project_root, "examples")
    
    # Find all JSON files in examples/
    json_files = glob.glob(os.path.join(examples_dir, "*.json"))
    
    if not json_files:
        print("No JSON files found in examples/ directory.")
        return

    print(f"Found {len(json_files)} example files.")
    
    success_count = 0
    
    for json_file in json_files:
        print(f"\nProcessing: {os.path.basename(json_file)}")
        result = run_pipeline(json_file)
        
        if result["status"] == "success":
            print(f"  [SUCCESS]")
            print(f"  Image: {result['image_path']}")
            print(f"  Doc:   {result['doc_path']}")
            success_count += 1
        else:
            print(f"  [FAILED]")
            print(f"  Error: {result['error']}")

    print(f"\nPipeline finished. {success_count}/{len(json_files)} successful.")

if __name__ == "__main__":
    main()

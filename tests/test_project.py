# tests/test_project.py
import unittest
import os
import sys
import json
import shutil

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.json_validator import validate_graph_json
from modules.main_pipeline import run_pipeline

class TestVLMGraphProject(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = "test_outputs"
        os.makedirs(self.test_dir, exist_ok=True)
        
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_validator_valid(self):
        data = {
            "graph_type": "line",
            "title": "Test Graph",
            "x_label": "X",
            "y_label": "Y",
            "data": [{"x": [1, 2], "y": [3, 4]}]
        }
        result = validate_graph_json(data)
        self.assertTrue(result["valid"])

    def test_validator_invalid_type(self):
        data = {
            "graph_type": "unknown_type",
            "data": []
        }
        result = validate_graph_json(data)
        self.assertFalse(result["valid"])
        self.assertIn("Unsupported graph_type", result["error"])

    def test_validator_missing_field(self):
        data = {
            "graph_type": "line",
            # Missing data, title, etc.
        }
        result = validate_graph_json(data)
        self.assertFalse(result["valid"])
        self.assertIn("Missing required field", result["error"])

    def test_pipeline_execution(self):
        # Create a temporary JSON file
        json_path = os.path.join(self.test_dir, "test_graph.json")
        data = {
            "graph_type": "bar",
            "title": "Test Bar",
            "x_label": "Category",
            "y_label": "Value",
            "data": [{"x": ["A", "B"], "y": [10, 20]}]
        }
        with open(json_path, 'w') as f:
            json.dump(data, f)
            
        # Run pipeline
        # We need to mock or adjust paths because pipeline uses hardcoded relative paths for outputs
        # But for now, let's see if it runs. The pipeline puts outputs in ../outputs relative to module.
        # This might clutter the real output directory, but it's acceptable for this simple test.
        
        result = run_pipeline(json_path)
        
        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.exists(result["image_path"]))
        self.assertTrue(os.path.exists(result["doc_path"]))

if __name__ == '__main__':
    unittest.main()

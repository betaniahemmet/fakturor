import sys
import os

# Get the absolute path of the project root
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Path to /tests/
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # Path to /fakturor/

# Add the root directory to sys.path
sys.path.insert(0, ROOT_DIR)

print(f"Added {ROOT_DIR} to sys.path")  # Debugging step
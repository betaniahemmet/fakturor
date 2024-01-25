from app.config import fakturor_path

from directory_tree import display_tree

# Specify the root directory of your project

directory_structure = display_tree(
    fakturor_path, ignore_list=["venv", "__pycache__"]
)
# Print the ASCII tree representation
print(directory_structure)

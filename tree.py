from directory_tree import display_tree
# Specify the root directory of your project

directory_structure = display_tree('C:/Users/henri/Documents/code/fakturor', ignore_list = ['venv'])
# Print the ASCII tree representation
print(directory_structure)

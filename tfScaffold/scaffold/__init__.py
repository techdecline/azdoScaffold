import os

def replace_in_files(folder_path, replacement_map):
    """
    Replace occurrences of keys with corresponding values in files within the specified folder
    and its subfolders recursively.

    Args:
    - folder_path (str): Path to the folder containing files.
    - replacement_map (dict): A dictionary where keys are strings to be replaced and values are their replacements.
    """
    # Iterate through the folder and its subfolders
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            
            # Read file content
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            # Replace occurrences in file content
            for key, value in replacement_map.items():
                file_content = file_content.replace(key, value)
            
            # Write modified content back to file
            with open(file_path, 'w') as file:
                file.write(file_content)

# # Example usage
# folder_path = "/path/to/folder"
# replacement_map = {
#     "old_string_1": "new_string_1",
#     "old_string_2": "new_string_2",
#     # Add more key-value pairs as needed
# }

# replace_in_files(folder_path, replacement_map)

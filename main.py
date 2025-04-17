import os

# Function to take user input for folder structure
def get_folder_structure():
    structure = {}
    
    while True:
        # Get main folder name
        main_folder = input("Enter the name of the main folder (or press Enter to stop): ").strip()
        if not main_folder:
            break
        
        structure[main_folder] = {}
        
        while True:
            # Ask for subfolder
            subfolder = input(f"Enter a subfolder inside {main_folder} (or press Enter to move to next main folder): ").strip()
            if not subfolder:
                break
            
            structure[main_folder][subfolder] = []
            
            while True:
                # Ask for files inside subfolder
                file_name = input(f"Enter a file name inside {subfolder} (or press Enter to finish this subfolder): ").strip()
                if not file_name:
                    break
                structure[main_folder][subfolder].append(file_name)
    
    return structure

# Prompt the user for the base directory (or use current directory)
base_dir = input("Enter the base directory (leave blank for current directory): ").strip() or os.getcwd()

# Get folder structure from user input
folder_structure = get_folder_structure()

# Function to create the folder structure based on user input
def create_structure(base, struct):
    for folder, contents in struct.items():
        folder_path = os.path.join(base, folder)
        os.makedirs(folder_path, exist_ok=True)  # Create the main folder
        for subfolder, files in contents.items():
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)  # Create subfolder if necessary
            for file in files:
                file_path = os.path.join(subfolder_path, file)
                open(file_path, 'a').close()  # Create empty file

# Call the function to create the structure in the provided directory
create_structure(base_dir, folder_structure)

print(f"? Folder and file structure created in {base_dir}")

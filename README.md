# Generic Folder Structure Creator

This Python script allows you to create a custom folder structure interactively. It enables users to define main folders, subfolders, and files for any type of project.

## Features
- Create a custom folder structure based on user input.
- Supports different folder names and file creation.
- Ideal for setting up project directories for any type of work (not just password managers).

## Usage
1. Clone this repository or download the `main.py` script.
2. Run the script by executing the following command:

    ```bash
    python main.py
    ```

3. You will be prompted to:
   - Enter the base directory where the structure will be created.
   - Define the folder names (main folders, subfolders, files).
   - The script will create the folder structure and corresponding empty files.

4. Example interaction:

    ```bash
    Enter the base directory (leave blank for current directory): ./my_project
    Enter the name of the main folder (or press Enter to stop): my_project
    Enter a subfolder inside my_project (or press Enter to move to next main folder): src
    Enter a file name inside src (or press Enter to finish this subfolder): main.cpp
    Enter a file name inside src (or press Enter to finish this subfolder): utils.cpp
    ```

## Requirements
- Python 3.x or later.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

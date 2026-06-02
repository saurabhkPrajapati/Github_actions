import os

def path_checker():
    # Full path of the currently running Python file
    file_path = os.path.abspath(__file__)

    # Directory where the file is located
    dir_path = os.path.dirname(file_path)

    # Folder name (last component of the directory path)
    folder_name = os.path.basename(dir_path)

    print("File path:", file_path)
    print("Directory path:", dir_path)
    print("Folder name:", folder_name)

path_checker()
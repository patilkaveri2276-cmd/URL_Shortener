import os
import shutil

# Ask user for folder path
path = input("Enter the folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp", ".c"],
    "Archives": [".zip", ".rar", ".tar"]
}

# Scan all files in directory
for file in os.listdir(path):
    
    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(file)[1].lower()

    moved = False

    for folder, extensions in file_types.items():
        if extension in extensions:

            folder_path = os.path.join(path, folder)

            # Create folder if not exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved {file} to {folder} folder")
            moved = True
            break

    # If file type not found
    if not moved:
        other_folder = os.path.join(path, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        shutil.move(file_path, os.path.join(other_folder, file))
        print(f"Moved {file} to Others folder")

print("File organization completed!")

import os
import shutil

# Set your desktop path
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

# Define folders for different file types
FOLDERS = {
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

# Temporary or unnecessary files
UNNECESSARY = [".tmp", ".log", ".ds_store"]


def organize_files():
    print("Organizing files...")
    for file in os.listdir(DESKTOP_PATH):
        file_path = os.path.join(DESKTOP_PATH, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FOLDERS.items():
                for ext in extensions:
                    if file.lower().endswith(ext):
                        folder_path = os.path.join(DESKTOP_PATH, folder)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        shutil.move(file_path, os.path.join(folder_path, file))
                        print(f"Moved {file} to {folder}")
                        moved = True
                        break
                if moved:
                    break
            if not moved:
                others_path = os.path.join(DESKTOP_PATH, "Others")
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(file_path, os.path.join(others_path, file))
                print(f"Moved {file} to Others")


def remove_unnecessary_files():
    print("Removing unnecessary files...")
    for root, _, files in os.walk(DESKTOP_PATH):
        for file in files:
            for ext in UNNECESSARY:
                if file.lower().endswith(ext):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted {file}")


def main():
    organize_files()
    remove_unnecessary_files()
    print("Desktop cleanup done!")


if __name__ == "__main__":
    main()

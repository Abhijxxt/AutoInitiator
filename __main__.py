import os

EXIT_CODE = 0       # 0 - normal, 1 or anything - error
PROJECT_PATH = ""
PROJECT_NAME = ""
GIT_REPOSITORY = ""
CONFIG_FILE = "./project_path.txt"

def get_project_path():
    global PROJECT_PATH
    if not PROJECT_PATH:
        # Try to read from config file
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                PROJECT_PATH = f.read().strip()
        # If still empty, prompt user and save
        if not PROJECT_PATH:
            PROJECT_PATH = input("Enter project path: ").strip()
            with open(CONFIG_FILE, "w") as f:
                f.write(PROJECT_PATH)

get_project_path()

print(PROJECT_PATH)
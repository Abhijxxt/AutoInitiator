import os, sys
import msvcrt       # For Windows-specific key handling

EXIT_CODE = 0       # 0 - normal, 1 or anything - error
PROJECT_PATH = ""
PROJECT_NAME = ""
GIT_REPOSITORY = ""
CONFIG_FILE = os.getcwd() + "\\project_path.txt"
# print(CONFIG_FILE)
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


def open_in_vscode():
    os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && code .")
    sys.exit(0)

def create_new_project():
    pass

def change_project_path():
    PROJECT_PATH = input("Enter project path: ").strip()
    with open(CONFIG_FILE, "w") as f:
        f.write(PROJECT_PATH)
    print(f"Project path changed to: {PROJECT_PATH}")

def terminal_start():
    print("1. Create a new project")
    print("2. Change the project path directory")
    print("3. Show current project path")
    print("4. Exit")

    choice = msvcrt.getch().decode("utf-8")
    if choice == '1':
        os.system("cls")
        create_new_project()
    elif choice == '2':
        os.system("cls")
        change_project_path()
    elif choice == '3':
        os.system("cls")
        print(f"Current project path: {PROJECT_PATH}")
    elif choice == '4':
        terminal_end()
    else:
        os.system("cls")
        print("Invalid choice. Please try again.")
    
    terminal_start()


def terminal_end():
    print("Exiting the script. Goodbye!")
    os.system("pause")
    sys.exit(0)

## WORKFLOW OF THE SCRIPT
print("----Welcome to AutoInitiator!----")
print("This script will help you set up a new project quickly.")
get_project_path()
terminal_start()
terminal_end()
print(PROJECT_PATH)
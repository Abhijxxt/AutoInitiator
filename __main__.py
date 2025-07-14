import os, sys
import msvcrt       # For Windows-specific key handling

EXIT_CODE = 0       # 0 - normal, 1 or anything - error
PROJECT_PATH = ""
PROJECT_NAME = ""
GIT_REPOSITORY = ""
CONFIG_FILE = "./project_path.txt"
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
    
def check_project_path():
    global PROJECT_PATH, EXIT_CODE
    if not os.path.exists(PROJECT_PATH):
        EXIT_CODE = os.system(f"mkdir {PROJECT_PATH}")
        if EXIT_CODE != 0:
            print("Failed to create project path. Please check permissions or path validity.")
            terminal_end()

def change_project_path():
    PROJECT_PATH = input("Enter project path: ").strip()
    with open(CONFIG_FILE, "w") as f:
        f.write(PROJECT_PATH)
    print(f"Project path changed to: {PROJECT_PATH}")
    print("Please restart the script to apply changes.")
    terminal_end()

def check_exit_code():
    if EXIT_CODE != 0:
        print("An error occurred during the setup process. Please check the commands and try again.")
        os.system("pause")
        sys.exit(EXIT_CODE)

def open_in_vscode():
    global PROJECT_PATH, PROJECT_NAME
    os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && code .")
    sys.exit(0)

def add_remote_repository():
    global GIT_REPOSITORY, PROJECT_PATH, PROJECT_NAME, EXIT_CODE
    GIT_REPOSITORY = input("Enter the remote Git repository URL: ").strip()
    if GIT_REPOSITORY:
        EXIT_CODE = os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && git remote add origin {GIT_REPOSITORY}")
        if EXIT_CODE != 0:
            os.system("cls")
            print("Failed to add remote repository. Please check the URL and try again.")
            after_creation_terminal()
        else:
            os.system("cls")
            print("Remote repository added successfully!")
            after_creation_terminal()

def init_git_repo():
    global PROJECT_PATH, PROJECT_NAME, EXIT_CODE
    EXIT_CODE = os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && git init")
    if EXIT_CODE != 0:
        os.system("cls")
        print("Failed to initialize Git repository. Please check the errors above.")
        after_creation_terminal()
    else:
        os.system("cls")
        print("Git repository initialized successfully!")
        print("1. Add remote repository")
        print("2. Back")
        choice = msvcrt.getch().decode("utf-8")
        if choice == '1':
            os.system("cls")
            add_remote_repository()
        elif choice == '2':
            os.system("cls")
            after_creation_terminal()
        else: 
            os.system("cls")
            print("Invalid choice. Please try again.")
            init_git_repo()
def check_project_name():
    global PROJECT_NAME
    for char in PROJECT_NAME:
        if char in ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '-', '@']:
            os.system("cls")
            print("Invalid project name. Please avoid using special characters.")
            create_new_project()

def create_project_dir():
    global PROJECT_PATH, PROJECT_NAME, EXIT_CODE
    EXIT_CODE = os.system(f"mkdir {PROJECT_PATH}\\{PROJECT_NAME}")
    if EXIT_CODE != 0:
        create_new_project()

def after_creation_terminal():
    print("Project setup completed successfully!")
    print("1. Open in VSCode")
    print("2. Initialize Git repository")
    print("3. Open terminal on created project")
    print("4. Return to main menu")
    print("5. Exit")
    choice = msvcrt.getch().decode("utf-8")
    if choice == '1':
        open_in_vscode()
    elif choice == '2':
        init_git_repo()
    elif choice == '4':
        os.system("cls")
        terminal_start()
    elif choice == '3':
        os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && start cmd")
        terminal_end()
    elif choice == '4':
        terminal_start()
    elif choice == '5':
        terminal_end()
    else:
        os.system("cls")
        print("Invalid choice. Please try again.")
    
    after_creation_terminal()
    
def project_type_handler():
    global EXIT_CODE 
    print("Enter the project type: ")
    print("1. React")
    print("2. Next.js")
    print("3. Node")
    print("4. Return to main menu")
    project_type = msvcrt.getch().decode("utf-8")
    if project_type == '1':
        EXIT_CODE += os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && npx create-react-app . -y") 
        after_creation_terminal() if EXIT_CODE == 0 else terminal_start()

    elif project_type == '2':
        EXIT_CODE += os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && npx create-next-app . -y")
        after_creation_terminal() if EXIT_CODE == 0 else terminal_start()

    elif project_type == '3':
        EXIT_CODE += os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && npm init -y")
        os.system(f"echo //start writing your code here > {PROJECT_PATH}\\{PROJECT_NAME}\\index.js")
        after_creation_terminal() if EXIT_CODE == 0 else terminal_start()

    elif project_type == '4':
        os.system("cls")
        terminal_start()
    else: 
        os.system("cls")
        print("Invalid choice. Please try again.")
        project_type_handler()

    check_exit_code()

def create_new_project():
    global PROJECT_NAME
    check_project_path()
    PROJECT_NAME = input("Enter the project name: ").strip().lower()
    check_project_name()
    create_project_dir()
    project_type_handler()



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
        os.system("cls")
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
os.system("cls")
print("----Welcome to AutoInitiator!----")
print("This script will help you set up a new project quickly.")
get_project_path()
terminal_start()
terminal_end()


## IN FUTURE
# Check path validity
# Add more project types
# Add more features like installing dependencies, etc.
# Add error handling for each command
# Add a configuration file to save default project path, dependencies and all
# Git integration
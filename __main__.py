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

def check_project_path():
    global PROJECT_PATH, EXIT_CODE
    if not os.path.exists(PROJECT_PATH):
        try:
            os.system(f"mkdir {PROJECT_PATH}")
        except:
            os.system("cls")
            print("Failed to create project path. Please check permissions or path validity.")
            terminal_end()

def change_project_path():
    PROJECT_PATH = input("Enter project path: ").strip()
    with open(CONFIG_FILE, "w") as f:
        f.write(PROJECT_PATH)
    print(f"Project path changed to: {PROJECT_PATH}")

def check_exit_code():
    if EXIT_CODE != 0:
        print("An error occurred during the setup process. Please check the commands and try again.")
        os.system("pause")
        sys.exit(EXIT_CODE)

def open_in_vscode():
    global PROJECT_PATH, PROJECT_NAME
    os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && code .")
    sys.exit(0)

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
        terminal_end()

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

    elif project_type == '2':
        EXIT_CODE += os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && npx create-next-app . -y")

    elif project_type == '3':
        EXIT_CODE += os.system(f"cd {PROJECT_PATH}\\{PROJECT_NAME} && npm init -y")
        os.system(f"echo //start writing your code here > {PROJECT_PATH}\\{PROJECT_NAME}\\index.js")
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
print("----Welcome to AutoInitiator!----")
print("This script will help you set up a new project quickly.")
get_project_path()
terminal_start()
terminal_end()
print(PROJECT_PATH)
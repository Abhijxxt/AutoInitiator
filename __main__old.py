import os
import sys
# print(os.name)
# os.system("start cmd")
exit_code = 0
def init_git_repo():
    os.system(f"cd {project_path}\\{project_name} && git init")
    git_url = input("Enter the remote Git repository URL (or leave blank to skip): ").strip()
    if git_url:
        exit_code += os.system(f"cd {project_path}\\{project_name} && git remote add origin {git_url}")
    else:
        print("Skipping remote repository setup.")

def open_in_vscode():
    os.system(f"cd {project_path}\\{project_name} && code .")
    sys.exit(0)

def exit_message(exit_code):
    if(exit_code == 0):
        print("Project setup completed successfully!")
    else:
        print("Project setup failed. Please check the errors above.")
    os.system("pause")
    os.system("exit")
    sys.exit(exit_code)

def check_project_path():
    if not os.path.exists(project_path):
        try:
            os.system(f"mkdir {project_path}")
        except:
            print("Failed to create project path. Please check permissions or path validity.")
            exit_message(1)

def check_exit_code():
    if exit_code != 0:
        print("An error occurred during the setup process. Please check the commands and try again.")
        exit_message(exit_code)
project_path = "D:\\WORK2"
check_project_path()
project_name = input("Enter the project name: ").strip().lower()
check_exit_code()

exit_code += os.system(f"mkdir {project_path}\\{project_name}")
if exit_code != 0:
    exit_message(exit_code)


def project_type():
    project_type = input("Enter the project type (e.g., react | node | next): ").strip().lower()

    if project_type == "react":
        exit_code += os.system(f"cd {project_path}\\{project_name} && npx create-react-app . -y") 

    elif project_type == "node":
        exit_code += os.system(f"cd {project_path}\\{project_name} && npm init -y")
        os.system(f"echo //start writing your code here > {project_path}\\{project_name}\\index.js")

    elif project_type == "next":
        exit_code += os.system(f"cd {project_path}\\{project_name} && npx create-next-app . -y")


    check_exit_code()

git_init_choice = input("Do you want to initialize a Git repository? (yes/no): ").strip().lower()
if git_init_choice == "yes":
    init_git_repo()

check_exit_code()    

vscode_choice = input("Do you want to open the project in VSCode? (yes/no): ").strip().lower()
if vscode_choice == "yes" or vscode_choice == "y":
    open_in_vscode()


exit_message(exit_code)

import os
print(os.name)
# Project Name
# Project file setup
# git init
# vs code opener (code .)

project_path = "D:\\WORK"

project_name = input("Enter the project name: ").strip().lower()
os.system(f"mkdir {project_path}\\{project_name}")

project_type = input("Enter the project type (e.g., react, node): ").strip().lower()
if project_type == "react":
    os.system(f"cd {project_path}\\{project_name} && npx create-react-app . -y") 
if project_type == "node":
    os.system(f"cd {project_path}\\{project_name} && npm init -y")
    os.system(f"echo > {project_path}\\{project_name}\\index.js")

os.system("echo Project setup complete!")
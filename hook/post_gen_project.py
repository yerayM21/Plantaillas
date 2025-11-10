import subprocess
import os 

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")

# Initvenv 
subprocess.call(["python", "-m", "venv", "venv"])

# Under env 
python_venv = os.getcwd()+"/venv/Scripts/python.exe"
subprocess.call([python_venv, "-m", "pip", "install", "--upgrade", "pip"])

subprocess.call(["-m","pip", "install", "-r", "requirements.txt"])

# Git init
if "{{ cookiecutter.init_git_repo }}" == "yes":
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Initial commit"])
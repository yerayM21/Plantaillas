#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
import shutil

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

def run(cmd, **kwargs):
    print(f"{MESSAGE_COLOR}$ {' '.join(cmd)}{RESET_ALL}")
    rc = subprocess.call(cmd, **kwargs)
    if rc != 0:
        sys.stderr.write(f"\nError: comando falló con código {rc}: {' '.join(cmd)}\n")
        sys.exit(rc)

print(f"{MESSAGE_COLOR}Almost done!{RESET_ALL}")

# 1) Crear venv con el mismo Python que ejecuta el hook
run([sys.executable, "-m", "venv", "venv"])

# 2) Resolver python del venv según SO
venv_dir = Path("venv")
if os.name == "nt":
    py_venv = venv_dir / "Scripts" / "python.exe"
else:
    py_venv = venv_dir / "bin" / "python"

if not py_venv.exists():
    sys.stderr.write(f"No se encontró el Python del venv en: {py_venv}\n")
    sys.exit(1)

# 3) Actualizar pip dentro del venv
run([str(py_venv), "-m", "pip", "install", "--upgrade", "pip"])

# 4) Instalar requirements si existe
req = Path("requirements.txt")
if req.exists():
    run([str(py_venv), "-m", "pip", "install", "-r", str(req)])
else:
    print("No requirements.txt — omitiendo instalación de dependencias.")

# 5) Git init (si el template lo pide)
if "{{ cookiecutter.init_git_repo }}" == "yes":
    if shutil.which("git"):
        run(["git", "init"])
        run(["git", "add", "."])
        run(["git", "commit", "-m", "Initial commit"])
    else:
        print("Git no encontrado en PATH — omitiendo inicialización de repo.")
else:
    print("Skipping git init as per user choice.")

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")

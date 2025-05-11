import subprocess
import os
from datetime import datetime

def run_script(script_name):
    print(f"Ejecutando {script_name}...")
    result = subprocess.run(["python3", script_name], cwd="backend")
    if result.returncode != 0:
        raise RuntimeError(f"Error al ejecutar {script_name}")

def git_push_frontend():
    print("Haciendo commit y push de la carpeta frontend...")
    os.chdir("frontend")
    
    subprocess.run(["git", "add", "."], check=True)
    
    commit_message = f"Actualización automática: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    
    subprocess.run(["git", "push"], check=True)
    
    os.chdir("..")

if __name__ == "__main__":
    try:
        run_script("crawler.py")
        run_script("writer.py")
        git_push_frontend()
        print("Despliegue completo.")
    except Exception as e:
        print(f"Error durante el despliegue: {e}")

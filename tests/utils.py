import os
import subprocess 


def run_flake8(path : str) -> str:
    cd = os.getenv("PWD")
    print(cd)
    flake_path = cd.replace("tests", "venv/bin/flake8")
    norm = subprocess.run([flake_path, path],
                   capture_output=True,
                   text=True
                   )

    print(norm.stdout)                   
    
    return norm.stdout

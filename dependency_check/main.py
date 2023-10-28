import subprocess
import os

def run_dependency_check():
    DC_VERSION = "6.5.0"
    DATA_DIRECTORY = "/usr/share/dependency-check/data"
    OUTPUT_DIRECTORY = "/report"
    OUTPUT_FILE = f"{OUTPUT_DIRECTORY}/dependency-check-report.json"

    # Criar diretórios de saída
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Construir o comando Docker
    command = [
        "docker", "run", "--rm",
        "-v", f"{os.getcwd()}:/src:z",
        "-v", f"{DATA_DIRECTORY}:/usr/share/dependency-check/data:z",
        "-v", f"{OUTPUT_DIRECTORY}:/report:z",
        f"owasp/dependency-check:{DC_VERSION}",
        "--scan", "/src",
        "--format", "JSON",
        "--out", OUTPUT_FILE
    ]

    # Executar o Dependency-Check
    subprocess.run(command, check=True)

if __name__ == "__main__":
    run_dependency_check()

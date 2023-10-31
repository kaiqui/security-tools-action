import subprocess
from loguru import logger
import sys
import os
from dependency_check.main import run_dependency_check
from trufflehog.main import find_leaks
from bandit_sast.main import sast_python
from checkov_iac.main import iac_test

def install_dependencies():
    logger.info("Instalando dependências...")
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run(["pip", "install", "bandit", "checkov"], check=True)
    logger.success("Dependências instaladas com sucesso.")

def run_tool(tool):
    output_file = f"{tool}-report.json"
    
    logger.info(f"Executando ferramenta: {tool}")
    if tool == "dependency-check":
        run_dependency_check()
    elif tool == "bandit":
        sast_python()
    elif tool == "checkov":
        iac_test()
    elif tool == "trufflehog":
        find_leaks() 
    else:
        logger.error(f"Ferramenta {tool} não reconhecida")
        sys.exit(1)
    logger.success(f"Ferramenta {tool} executada com sucesso.")

def main():
    logger.info("Iniciando o script de ferramentas de segurança...")

    tools_input = os.getenv("TOOL")
    if tools_input:
        logger.info(f"Rodando a(s) ferramenta(s): {tools_input}")
        tools = {
            "all": ["dependency-check", "bandit", "checkov"],
            "web": ["bandit", "trufflehog"],
            "iac": ["checkov"],
            "mobile": [],
            "android": [],
            "ios": [],
        }.get(tools_input, tools_input.split(","))

        for tool in tools:
            run_tool(tool.strip())

        logger.success("Todas as ferramentas foram executadas com sucesso.")
    else:
        logger.exception("Favor informar o tipo de ferramenta")
        sys.exit(1)

if __name__ == "__main__":
    main()

import subprocess
from loguru import logger
import sys
import os
from dependency_check.main import run_dependency_check

def install_dependencies():
    logger.info("Instalando dependências...")
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run(["pip", "install", "bandit", "checkov"], check=True)
    logger.success("Dependências instaladas com sucesso.")

def run_tool(tool):
    logger.info(f"Executando ferramenta: {tool}")
    if tool == "dependency-check":
        run_dependency_check()
    elif tool == "bandit":
        subprocess.run(["bandit", "-r", ".", "-f", "json", "-o", "bandit-report.json"], check=True)
    elif tool == "checkov":
        subprocess.run(["checkov", "-d", ".", "-o", "json", "--output-file", "checkov-report.json"], check=True)
    else:
        logger.error(f"Ferramenta {tool} não reconhecida")
        sys.exit(1)
    logger.success(f"Ferramenta {tool} executada com sucesso.")

def main():
    logger.info("Iniciando o script de ferramentas de segurança...")

    tools_input = os.getenv("TOOL")
    if tools_input:
        logger.info(f"Rodando a ferramenta: {tools_input}")
        tools = {
            "all": ["dependency-check", "bandit", "checkov"],
            "web": ["bandit"],
            "iac": ["checkov"],
            "mobile": [],
            "android": [],
            "ios": [],
        }.get(tools_input, tools_input.split(","))

        for tool in tools:
            run_tool(tool.strip())

        logger.success("Todas as ferramentas foram executadas com sucesso.")
    else:
        logger.error("informe o tipo de ferramenta: {tools_input}")

if __name__ == "__main__":
    logger.info(
        """\n
 _______  _______  _______  _______  ___   _______  _______  _______  _______  _______  ___      _______ 
|       ||       ||       ||       ||   | |       ||       ||       ||       ||       ||   |    |       |
|  _____||    ___||       ||    _  ||   | |    _  ||    ___||_     _||   _   ||   _   ||   |    |  _____|
| |_____ |   |___ |       ||   |_| ||   | |   |_| ||   |___   |   |  |  | |  ||  | |  ||   |    | |_____ 
|_____  ||    ___||      _||    ___||   | |    ___||    ___|  |   |  |  |_|  ||  |_|  ||   |___ |_____  |
 _____| ||   |___ |     |_ |   |    |   | |   |    |   |___   |   |  |       ||       ||       | _____| |
|_______||_______||_______||___|    |___| |___|    |_______|  |___|  |_______||_______||_______||_______|
        
Author: kaiqui 
Version: 0.1
        \n"""
    )
    main()

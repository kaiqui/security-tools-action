import subprocess
from loguru import logger
import sys
import os
from safety_dependency.main import dependency_analise
from trufflehog.main import find_leaks
from bandit_sast.main import sast_python
from checkov_iac.main import iac_test


def run_tool(tool):    
    logger.info(f"Executando ferramenta: {tool}")
    if tool == "safety":
        dependency_analise()
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
            "web": ["bandit", "trufflehog", "safety"],
            "iac": ["checkov","trufflehog"],
            "mobile": ["trufflehog"],
            "android": ["trufflehog"],
            "ios": ["trufflehog"],
        }.get(tools_input, tools_input.split(","))

        for tool in tools:
            run_tool(tool.strip())

        logger.success("Todas as ferramentas foram executadas com sucesso.")
    else:
        logger.exception("Favor informar o tipo de ferramenta")
        sys.exit(1)

if __name__ == "__main__":
    main()

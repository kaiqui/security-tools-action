import os
import subprocess
from loguru import logger


def iac_test():
    output_file = 'checkov-report.json'
    subprocess.run(["checkov", "-d", ".", "-o", "json", "--output-file", output_file], check=False)
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            content = file.read()
            logger.info(f"Conteúdo de {output_file}:\n{content}")
    else:
        logger.warning(f"Arquivo de saída {output_file} não encontrado")
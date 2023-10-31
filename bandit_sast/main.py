import os
import subprocess
from loguru import logger
import json


def sast_python():
    output_file = 'bandit-report.json'
    subprocess.run(["python","-m","bandit", "-r", ".", "-f", "json", ">", output_file], check=False)
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            content = file.read()
            result_sast = json.loads(content)
            logger.info(f"Conteúdo de {output_file}:\n{result_sast['results']}")
    else:
        logger.warning(f"Arquivo de saída {output_file} não encontrado")
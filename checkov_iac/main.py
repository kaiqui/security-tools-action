import os
import subprocess
from loguru import logger
import json

def iac_test():
    output_file = 'checkov_report/results_json.json'
    result = subprocess.run(["checkov", "-d", ".", "-o", "json", "--output-file", 'checkov_report'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if result.stderr:
        logger.info(result.stderr)
    elif result.stdout:
        logger.info(result.stdout)
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            content = file.read()
            result_iac = json.loads(content)
            if 'results' in result_iac and 'failed_checks' in result_iac['results']:
                failed_checks = result_iac['results']['failed_checks']
                for check in failed_checks:
                    check_id = check.get('check_id', 'Não informado')
                    check_name = check.get('check_name', 'Não informado')
                    file_path = check.get('file_path', 'Não informado')
                    file_line_range = check.get('file_line_range', 'Não informado')
                    guideline = check.get('guideline', 'Não informado')
                    
                    logger.error(f"Check ID: {check_id}\n"
                                 f"Check Name: {check_name}\n"
                                 f"File Path: {file_path}\n"
                                 f"File Line Range: {file_line_range}\n"
                                 f"Guideline: {guideline}")
            else:
                logger.warning(f"Chaves 'results' ou 'failed_checks' não encontradas no arquivo de resultado {output_file}")
    else:
        logger.warning(f"Arquivo de saída {output_file} não encontrado")
        
iac_test()

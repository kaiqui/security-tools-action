import os
import subprocess
from loguru import logger
import json

def dependency_analise():
    output_file = 'safety_report.json'
    
    # Executa o comando safety e salva o resultado em safety_report.json
    command = ["safety", "check", "--output", "json"]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    try:
        result_safety = json.loads(result.stdout)
    except json.JSONDecodeError:
        logger.error("Falha ao decodificar o JSON do resultado do safety.")
        return
    if "vulnerabilities" in result_safety:
        log_vulnerabilities(result_safety["vulnerabilities"])
    else:
        logger.warning(f"Chave 'vulnerabilities' não encontrada no arquivo de resultado {output_file}")

def log_vulnerabilities(vulnerabilities):
    if not vulnerabilities:
        logger.info("No vulnerabilities found.")
        return

    for idx, vulnerability in enumerate(vulnerabilities, start=1):
        logger.info(f"Vulnerability {idx}:")
        logger.info(f" - Vulnerability ID: {vulnerability.get('vulnerability_id', 'Not provided')}")
        logger.info(f" - Package Name: {vulnerability.get('package_name', 'Not provided')}")
        logger.info(f" - Ignored: {vulnerability.get('ignored', 'Not provided')}")
        logger.info(f" - Ignored Reason: {vulnerability.get('ignored_reason', 'Not provided')}")
        logger.info(f" - Ignored Expires: {vulnerability.get('ignored_expires', 'Not provided')}")
        logger.info(f" - Vulnerable Spec: {vulnerability.get('vulnerable_spec', 'Not provided')}")
        logger.info(f" - All Vulnerable Specs: {vulnerability.get('all_vulnerable_specs', 'Not provided')}")
        logger.info(f" - Analyzed Version: {vulnerability.get('analyzed_version', 'Not provided')}")
        logger.info(f" - Advisory: {vulnerability.get('advisory', 'Not provided')}")
        logger.info(f" - Is Transitive: {vulnerability.get('is_transitive', 'Not provided')}")
        logger.info(f" - Published Date: {vulnerability.get('published_date', 'Not provided')}")
        logger.info(f" - Fixed Versions: {vulnerability.get('fixed_versions', 'Not provided')}")
        logger.info(f" - Closest Versions Without Known Vulnerabilities: {vulnerability.get('closest_versions_without_known_vulnerabilities', 'Not provided')}")
        logger.info(f" - Resources: {vulnerability.get('resources', 'Not provided')}")
        logger.info(f" - CVE: {vulnerability.get('CVE', 'Not provided')}")
        logger.info(f" - Severity: {vulnerability.get('severity', 'Not provided')}")
        logger.info(f" - Affected Versions: {vulnerability.get('affected_versions', 'Not provided')}")
        logger.info(f" - More Info URL: {vulnerability.get('more_info_url', 'Not provided')}")
        logger.info("")

if __name__ == "__main__":
    dependency_analise()

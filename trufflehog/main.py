import subprocess
import pathlib
import json
import os
from loguru import logger

def find_leaks():
    PATH = str(pathlib.Path().parent.resolve())
    GH_LOGIN = os.getenv("LOGIN")
    TOKEN = os.getenv("API_TOKEN")
    org = os.getenv("GITHUB_REPOSITORY_OWNER")
    app = os.getenv("GITHUB_REPOSITORY").split("/")[-1]
    
    conn = f'https://{GH_LOGIN}:{TOKEN}@github.com/{org}/{app}.git'
    cmd = (f'docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest git {conn} --json',
           '> trufflehog-report.json')
    cmd = " ".join(str(item) for item in cmd)
    logger.info(cmd)
    result = subprocess.run(cmd, shell=True)
    if result.returncode >= 0:
        with open(f'{PATH}/trufflehog-report.json', 'r') as f:
            out_json = json.loads(
                "[" + f.read().replace("}\n{", "},\n{") + "]")
        for j in range(len(out_json)):
            try:
                commit_hash = out_json[j]['SourceMetadata']['Data']['Git']['commit']
                date_commit = out_json[j]['SourceMetadata']['Data']['Git']['timestamp']
                date_commit = date_commit[0:19]
                path = out_json[j]['SourceMetadata']['Data']['Git']['file']
                reason = out_json[j]['DetectorName']
                payload = {
                    'commit_hash': commit_hash,
                    'path': path,
                    'reason': reason,
                    'leak': out_json[j]['Raw']
                }
                logger.info(f"Leak found: {payload}")
            except Exception as e:
                logger.warning(e)
                continue
    else:
        logger.error(f'RETURN CODE: {result.returncode}')
        return False
    return True
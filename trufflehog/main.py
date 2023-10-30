import subprocess
import pathlib
import json
import os
from loguru import logger

def find_leaks():
    PATH = str(pathlib.Path().parent.resolve())
    G_USERNAME = os.environ.get("G_USERNAME")
    G_TOKEN = os.environ.get("G_TOKEN")
    org = os.environ.get("GITHUB_REPOSITORY_OWNER")
    app = os.environ.get("GITHUB_REPOSITORY").split("/")[-1]
    logger.info(G_USERNAME)
    logger.info(G_TOKEN)
    logger.info(org)
    logger.info(app) 
    
    conn = f'https://{G_USERNAME}:{G_TOKEN}@github.com/{org}/{app}.git'
    logger.info(conn)
    cmd = (f'docker run --rm -i -v "$PWD:/pwd" trufflesecurity/trufflehog:latest git {conn} --json',
           '> trufflehog-report.json')
    cmd = " ".join(str(item) for item in cmd)
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

find_leaks()
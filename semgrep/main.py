import subprocess
import os
from loguru import logger
import sys

def sast_scan():
    SEMGREP_APP_TOKEN = os.environ.get("SEMGREP_APP_TOKEN")
    if SEMGREP_APP_TOKEN:
        return subprocess.run(["docker", "run", f"SEMGREP_APP_TOKEN={SEMGREP_APP_TOKEN}", "--rm", "-v", '"${PWD}:/src"', "returntocorp/semgrep", "ci"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    logger.error('SEMGREP_APP_TOKEN is not defined')
    sys.exit(1)
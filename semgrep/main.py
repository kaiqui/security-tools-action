import subprocess
import os
from loguru import logger
import sys

def sast_scan():
    SEMGREP_TOKEN = os.getenv("SEMGREP_TOKEN")
    if SEMGREP_TOKEN:
        return subprocess.run(["docker", "run", f"SEMGREP_APP_TOKEN={SEMGREP_TOKEN}", "--rm", "-v", '"${PWD}:/src"', "returntocorp/semgrep", "ci"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    logger.error('SEMGREP_TOKEN is not defined')
    sys.exit(1)
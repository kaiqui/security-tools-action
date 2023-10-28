import subprocess
import sys
import os
from dependency_check.main import run_dependency_check

def install_dependencies():
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run(["pip", "install", "bandit", "checkov"], check=True)

def run_tool(tool):
    if tool == "dependency-check":
        run_dependency_check()
    elif tool == "bandit":
        subprocess.run(["python", "-m", "bandit", "-r", ".", "-f", "json", "-o", "reports/bandit-report.json"], check=True)
    elif tool == "checkov":
        subprocess.run(["checkov", "-d", ".", "-o", "json", "--output-file", "reports/checkov-report.json"], check=True)
    else:
        print(f"Tool {tool} not recognized")
        sys.exit(1)

def main():
    install_dependencies()

    tools_input = os.getenv("INPUT_TOOLS", "all")
    tools = {
        "all": ["dependency-check", "bandit", "checkov"],
        "web": [ "bandit"],
        "iac": ["checkov"],
        "mobile": [],
        "android": [],
        "ios": [],
    }.get(tools_input, tools_input.split(","))

    for tool in tools:
        run_tool(tool.strip())

if __name__ == "__main__":
    main()

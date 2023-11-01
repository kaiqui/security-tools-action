import subprocess
import os

def run_dependency_check():
    DC_VERSION = "8.4.2"
    DC_DIRECTORY = os.path.expanduser("~/OWASP-Dependency-Check")
    DC_PROJECT = "dependency-check scan"
    DATA_DIRECTORY = f"{DC_DIRECTORY}/data"
    CACHE_DIRECTORY = f"{DC_DIRECTORY}/data/cache"

    # Obtem o diretório de trabalho atual
    current_directory = os.getcwd()
    
    # Obtem o usuário atual e o grupo
    user_id = os.getuid()
    group_id = os.getgid()

    command = [
        'docker', 'run', '--rm',
        '-e', f'user={os.environ.get("USER")}',
        '-u', f'{user_id}:{group_id}',
        '--volume', f'{current_directory}:/src:z',
        '--volume', f'{DATA_DIRECTORY}:/usr/share/dependency-check/data:z',
        '--volume', f'{current_directory}/odc-reports:/report:z',
        f'owasp/dependency-check:{DC_VERSION}',
        '--scan', '.',
        '--format', 'ALL',
        '--project', DC_PROJECT,
        '--out', '/report'
    ]
    print(' '.join(command))

    subprocess.run(command, check=True)


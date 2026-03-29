import os
import enum
from typing import Any, Callable
from pathlib import Path

HELP_TEXT = """
Usage:
    ./run.sh <target> <command> [arguments]

Targets:
    all
        Run command on all configured servers.

    <server_name>
        Run command on a single server.

    <server1,server2,...>
        Run command on multiple selected servers.

Examples:
    ./run.sh all disk
    ./run.sh web01 uptime
    ./run.sh web01,db01 backup /var/log/mysql
    ./run.sh game01 exec "df -h"


Commands:

    exec <command>
        Executes raw shell command on remote servers.

    backup <path>
        Creates backup of remote path and downloads it to local /backup directory.

    upload <local_file> <remote_directory>
        Uploads file from local machine to remote server directory.

    disk
        Shows disk usage (df -h).

    uptime
        Shows system uptime.

    hostname
        Shows hostname of remote server.

    memory
        Shows memory usage.

    service <name>
        Shows status of given service.

    last <flag>
        Shows command history in current program instance.

        Flags:
            cmd
                Shows last executed commands.

            out
                Shows last commands with their output.
"""

def singletonclass(cls: Any) -> Callable:
    instance: dict[Any, Any] = {}

    def wrapper(*args, **kwargs):
        if not cls in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper

class LogLevel(enum.Enum):
    LOG_LEVEL_NONE = 0
    LOG_LEVEL_LOG = 1
    LOG_LEVEL_WARNING = 2
    LOG_LEVEL_ERROR = 3
    LOG_LEVEL_MAX_NUM = 4

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

log_level_to_name = {
    LogLevel.LOG_LEVEL_LOG.value: f"{GREEN}<Log>{RESET}",
    LogLevel.LOG_LEVEL_WARNING.value: f"{YELLOW}<Warning>{RESET}",
    LogLevel.LOG_LEVEL_ERROR.value: f"{RED}<Error>{RESET}"
}

log_files = {
    "log": ["syslog.txt", "sysserr.txt"],
    "server_log": ["cmd_log.txt"]
}

def get_project_root(project_name="sentinel") -> Path:
    current_path = Path(__file__).resolve()
    for parent in [current_path] + list(current_path.parents):
        if parent.name.lower() == project_name.lower():
            return parent

    return Path.cwd()

PROJECT_DIR = get_project_root("sentinel")

def get_full_path(root_folder: str, file: str) -> str:
    return os.path.join(PROJECT_DIR, root_folder, file)

def check_existing_file_in_root_folder(root_folder: str, file: str) -> bool:
    fp = get_full_path(root_folder, file)
    return os.path.exists(fp)

def get_working_dir(directory: str) -> Path:
    return PROJECT_DIR / directory.strip("/")

def create_missing_file(root_folder: str, file: str) -> bool:
    target_dir = get_working_dir(root_folder)
    file_path = target_dir / file
    
    max_attempts = 3
    while max_attempts > 0:
        if file_path.exists():
            return True

        try:
            target_dir.mkdir(parents=True, exist_ok=True)
            file_path.touch(exist_ok=True)
            return True
        except Exception as e:
            max_attempts -= 1
            print(f"Error: {e}")
    
    return False
if __name__ == '__main__':

    print(f"Project Root: {PROJECT_DIR}")
    print(create_missing_file('logs', 'syslog.txt'))


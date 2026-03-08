import os

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

PROJECT_DIR: str = os.getcwd()

def get_working_dir(directory: str) -> str:
    return os.path.join(PROJECT_DIR, directory)

if __name__ == '__main__':
    print(f"working dir: {get_working_dir('core')}")

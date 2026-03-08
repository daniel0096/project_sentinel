# Sentinel

Sentinel is a simple Python CLI tool for executing commands and administrative actions on multiple remote Linux / FreeBSD servers over SSH.

The tool loads server configuration from JSON files and allows you to run commands or predefined actions across all or selected servers.

Sentinel is designed as a lightweight infrastructure utility for system administrators and DevOps workflows.

---

# Features

Current capabilities include:

- Execute raw shell commands on remote servers
- Run predefined administrative actions
- Target:
  - all servers
  - a single server
  - multiple selected servers
- SSH key authentication
- File upload to remote servers
- Remote backups
- Disk usage checks
- Command history tracking during runtime

Future improvements may include:

- parallel execution
- persistent SSH connections
- log collection
- service monitoring
- automated deployments

---

# Requirements

- Python 3.10+
- SSH client installed
- Access to remote servers via SSH
- Optional: SSH keys configured

---

# Installation

Clone the repository:

```bash
git clone https://github.com/daniel0096/project_sentinel.git
cd project_sentinel
```
Make sure python is available:

```bash
python3 --version
```

# Running the tool
Sentinel is launched through the run.sh wrapper.

Example usage
```bash

# Running built-in commands

./run.sh all disk
./run.sh server_db uptime
./run.sh server_web, server_db, server_db01 backup /var/log/mysql

# Running raw commands inside of the server

./run.sh server_web exec "awk -F: '{print $1}' /etc/passwd"
./run.sh server_web,server_db exec "ls -l /etc/"
./run.sh all exec "df -h"

```
# Command syntax

```bash
./run.sh <target> <command> [args...]
```

# Targets

```bash
all
    Run command on all configured servers.

<server_name>
    Run ommand on a single server.

<server1,server2,server3,...>
    Run command on multiple selected servers.

```




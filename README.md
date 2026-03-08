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
git clone https://github.com/yourname/sentinel.git
cd sentinel

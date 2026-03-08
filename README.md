# Sentinel

Sentinel is a simple Python CLI tool for executing commands and
administrative actions on multiple remote Linux / FreeBSD servers over
SSH.

The tool loads server configuration from JSON files and allows you to
run commands or predefined actions across all or selected servers.

Sentinel is designed as a lightweight infrastructure utility for system
administrators and DevOps workflows.

------------------------------------------------------------------------

# Features

Current capabilities include:

-   Execute raw shell commands on remote servers
-   Run predefined administrative actions
-   Target:
    -   all servers
    -   a single server
    -   multiple selected servers
-   SSH key authentication
-   File upload to remote servers
-   Remote backups
-   Disk usage checks
-   Command history tracking during runtime

Future improvements may include:

-   parallel execution
-   persistent SSH connections
-   log collection
-   service monitoring
-   automated deployments

------------------------------------------------------------------------

# Requirements

-   Python 3.10+
-   SSH client installed
-   Access to remote servers via SSH
-   Optional: SSH keys configured

------------------------------------------------------------------------

# Installation

Clone the repository:

    git clone https://github.com/yourname/sentinel.git
    cd sentinel

Make sure Python is available:

    python3 --version

------------------------------------------------------------------------

# Running the Tool

Sentinel is launched through the `run.sh` wrapper script.

Example:

    ./run.sh all disk
    ./run.sh web01 uptime
    ./run.sh web01,db01 backup /var/log/mysql
    ./run.sh game01 exec "df -h"

------------------------------------------------------------------------

# Command Syntax
a
    ./run.sh <target> <command> [arguments]

## Targets

    all
        Run command on all configured servers.

    <server_name>
        Run command on a single server.

    <server1,server2,...>
        Run command on multiple selected servers.

Example:

    ./run.sh all disk
    ./run.sh web01 uptime
    ./run.sh web01,db01 exec "df -h"

------------------------------------------------------------------------

# Commands

## Raw execution

    exec <command>

Executes a raw shell command on the remote servers.

Example:

    ./run.sh all exec "df -h"
    ./run.sh web01 exec "uptime"

------------------------------------------------------------------------

## Backup

    backup <path>

Creates a remote archive of the given path and downloads it to the local
`/backup` directory.

Example:

    ./run.sh web01 backup /var/log/mysql

------------------------------------------------------------------------

## Upload

    upload <local_file> <remote_directory>

Uploads a file from the local machine to the remote server.

Example:

    ./run.sh web01 upload backup.sql /tmp

------------------------------------------------------------------------

## Disk usage

    disk

Shows disk usage on the remote server.

Equivalent command:

    df -h

Example:

    ./run.sh all disk

------------------------------------------------------------------------

## Uptime

    uptime

Shows system uptime.

Example:

    ./run.sh web01 uptime

------------------------------------------------------------------------

## Hostname

    hostname

Shows hostname of the remote server.

Example:

    ./run.sh all hostname

------------------------------------------------------------------------

## Memory usage

    memory

Displays RAM usage.

Example:

    ./run.sh web01 memory

------------------------------------------------------------------------

## Service status

    service <name>

Checks the status of a service.

Example:

    ./run.sh web01 service nginx

------------------------------------------------------------------------

## Command history

    last <flag>

Displays commands executed during the current runtime session.

Flags:

    cmd
        Shows last executed commands.

    out
        Shows commands with their output.

Example:

    ./run.sh last cmd
    ./run.sh last out

------------------------------------------------------------------------

# Server Configuration

Servers are defined in JSON configuration files located in:

    config_files/

Example configuration:


```json
{
  "servers": [
    {
      "name": "web01",
      "ip_addr": "192.168.1.10",
      "ssh_port": 22,
      "user": "root",
      "ssh_connection_type": "ssh_key",
      "ssh_key_path": "~/.ssh/id_rsa",
      "os": "linux"
    }
  ]
}


```

Fields:

| Field | Description |
|------|-------------|
| name | unique server identifier |
| ip_addr | server IP address |
| ssh_port | SSH port (default 22) |
| user | SSH user |
| ssh_connection_type | authentication type |
| ssh_key_path | path to SSH key |
| os | server operating system |
name unique server identifier

------------------------------------------------------------------------

# Installing Sentinel as a CLI command

You can install Sentinel so it can be executed globally as:

    sentinel ...

## Step 1

Move the project somewhere permanent:

    /opt/sentinel

Example:

    sudo mkdir /opt/sentinel
    sudo cp -r * /opt/sentinel

------------------------------------------------------------------------

## Step 2

Create a launcher script:

    /usr/local/bin/sentinel

    sudo nano /usr/local/bin/sentinel

Add:

#!/usr/bin/env bash python3 /opt/sentinel/core/main.py "\$@"

------------------------------------------------------------------------

## Step 3

Make it executable:

    sudo chmod +x /usr/local/bin/sentinel

------------------------------------------------------------------------

## Step 4

Now the tool can be executed globally:

    sentinel all disk
    sentinel web01 uptime
    sentinel web01 exec "df -h"

------------------------------------------------------------------------
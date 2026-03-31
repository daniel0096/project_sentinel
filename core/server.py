from json_loader import JsonLoader

from utils import log_files, LogLevel
from core_log import CORE_TRACE_LOG, Log

class Server:
    def __init__(self):
        self._server_data: JsonLoader = JsonLoader()
        self._server_data.find_json()
        self._server_data.load_data()

    def parse_command(self, cmd: str) -> dict:
        split_cmd: list[str] = cmd.split()

        if len(split_cmd) < 2:
            return {"error" : "Invalid command. Usage - <target> <command> [args...]"}

        target, command, *args = split_cmd

        return {
            "target" : target,
            "command" : command,
            "args" : args
        }

    def run_cmd(self, cmd: str) -> bool:

        parsed = self.parse_command(cmd)

        if "error" in parsed:
            print(parsed["error"])
            return False

        target = parsed["target"]
        command = parsed["command"]
        args = parsed["args"]

        data: list[dict[str, object]] = self._server_data.json_data
        success = False

        if target == "all":
            target_servers = data
        else:
            targets = target.split(",")
            target_servers = [s for s in data if s.get("name") in targets]

            if not target_servers:
                CORE_TRACE_LOG(LogLevel.LOG_LEVEL_ERROR.value, f"No matching servers found for target: {target}")
                return False

        match command:
            case "exec":
                remote_cmd = " ".join(args)
            case "disk":
                remote_cmd = "df -h"
            case "uptime":
                remote_cmd = "uptime"
            case "hostname":
                remote_cmd = "hostname"
            case _:
                CORE_TRACE_LOG(LogLevel.LOG_LEVEL_ERROR.value, f"Unknown command: {command}")
                return False

        for server in target_servers:
            server_name = server.get("name")
            server_ip = server.get("ip_addr")
            server_port = server.get("ssh_port", 22)
            server_user = server.get("user", "root")
            server_connection_type = server.get("ssh_connection_type")

            ssh_command = [
                "ssh",
                "-p",
                str(server_port),
                f"{server_user}@{server_ip}",
                remote_cmd
            ]

            if server_connection_type == "ssh_key":
                key_path = server.get("ssh_key_path")

                if key_path:
                    ssh_command.insert(1, "-i")
                    ssh_command.insert(2, key_path)
                else:
                    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_ERROR.value, f"Missing ssh key for server {server_name}")
                    continue

            CORE_TRACE_LOG(LogLevel.LOG_LEVEL_LOG.value, f"Running on {server_name}: {remote_cmd}")

            cmd_log_file = log_files.get('server_log')[0]

            logger = Log()

            logger.run_process_to_log_file(
                filename=cmd_log_file,
                header=f"\n--- Output from {server_name} ---",
                command=ssh_command
            )
        return success
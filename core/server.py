from json_loader import JsonLoader

import subprocess


class Server:
    def __init__(self):
        self._server_data: JsonLoader = JsonLoader()
        self._server_data.find_json()
        self._server_data.load_data()

    def run_cmd(self, cmd: str) -> bool:
        data: list[dict[str, object]] = self._server_data.json_data
        success = False

        "TODO: implement connection history, when linked list is finished"

        for server in data:
            server_name = server.get("name")
            server_ip = server.get("ip_addr")
            server_port = server.get("ssh_port", 22) # default 22
            server_os = server.get("os")
            server_connection_type = server.get("ssh_connection_type")
            server_user = server.get("user", "root")
        
            ssh_command = ["ssh", "-p", str(server_port), f"{server_user}@{server_ip}", f"{cmd}"]

            if server_connection_type == "ssh_key":
                key_path = server.get("ssh_key_path")

                if key_path:
                    ssh_command.insert(1, "-i")
                    ssh_command.insert(2, f"{key_path}")
                else:
                    print(f"Key path error, ssh key required by connection type to server {server_name} was not specified.")
                    continue
            
            elif server_connection_type == "password":
                print(f"Connection to server {server_name} requires password.")

            print(f"Connecting to {server_name} as {server_user}@{server_ip}:{server_port}.")
            try:
                subprocess.run(ssh_command,check=True)
                success = True
            except subprocess.CalledProcessError as err:
                print(f"Could not connect to the server {server_name}, an error ocured: {err}")
            except FileNotFoundError:
                print(f"Given command was not found on your system.")

        return success
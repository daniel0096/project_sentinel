import json
import os
import shutil
from utils import get_working_dir
import subprocess
from typing import Optional

class JsonLoader:
    def __init__(self):
        self._json_files: list = []
        self._json_data: list = []
        self._config_dir: str = get_working_dir("config_files")
        self._servers_file: str = os.path.join(self._config_dir, "servers.json")
        self._servers_sample_file: str = os.path.join(self._config_dir, "servers.sample.json")

    def _ensure_servers_file(self) -> None:
        """
        Create servers.json from servers.sample.json if missing.
        """
        if os.path.exists(self._servers_file):
            return

        if os.path.exists(self._servers_sample_file):
            shutil.copyfile(self._servers_sample_file, self._servers_file)

    def find_json(self) -> list[str]:
        self._ensure_servers_file()
        try:
            res = subprocess.run(["find", self._config_dir ,"-type", "f", "-name", "*.json"], capture_output=True, text=True, check=True)
            lines = res.stdout.strip().splitlines()

            for line in lines:
                if line.endswith(".sample.json"):
                    continue
                if not line in self._json_files:
                    self._json_files.append(line)
                    
            return self._json_files

        except subprocess.CalledProcessError as subprocessErr:
            print(f"Linux find command failed with code {subprocessErr.returncode}: {subprocessErr.stderr}")
            return []

    def json_file(self, index: int) -> Optional[str]:
        """
        Return specific json file by index.
        """
        return self._json_files[index] if index < len(self._json_files) else None

    @property
    def json_data(self) -> list[dict]:
        return self._json_data if len(self._json_data) > 0 else []

    def load_data(self) -> bool:
        self._json_data.clear()
        try:
            for file_path in self._json_files:
                with open(file_path, mode="r", encoding="utf-8") as json_data:
                    content = json.load(json_data)
                    servers = content.get("servers", [])

                    for server in servers:
                        self._json_data.append(server)

            return True

        except FileNotFoundError as err:
            print(err)
            return False

if __name__ == '__main__':
    """
    Inplace debug purposes
    """
    
    

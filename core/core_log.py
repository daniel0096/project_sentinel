from utils import\
(
    LogLevel,
    log_files,
    create_missing_file,
    get_working_dir,
    log_level_to_name,
    singletonclass
)

from datetime import datetime
import subprocess
from pathlib import Path

@singletonclass
class Log:
    def __init__(self):
        self.log_files = log_files.get('log', [])

    def _get_log_path(self, filename: str) -> Path:
        if not create_missing_file('logs', filename):
            return None
        return get_working_dir("logs") / filename

    def _write_line(self, filename: str, text: str) -> bool:
        fp = self._get_log_path(filename)
        if fp is None:
            return False

        try:
            with open(fp, "a", encoding="utf-8") as f:
                f.write(text + "\n")
            return True

        except Exception as err:
            print(f"Error while writing to a file {err}")
            return False

    def append(self, level: int, message: str):
        target_file = ""

        log_label = log_level_to_name.get(level, "<Unknown>")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        match level:
            case LogLevel.LOG_LEVEL_LOG.value |\
                 LogLevel.LOG_LEVEL_WARNING.value:

                target_file = self.log_files[0]
            case LogLevel.LOG_LEVEL_ERROR.value:
                target_file = self.log_files[1]
            case _:
                print("Unknown level.")
                return False

        if create_missing_file('logs', target_file):
            self._write_line(target_file, f"{timestamp} {log_label}: {message}")
            return True

        return False

    def run_process_to_log_file(self, filename:str, header: str, command: list[str]) -> bool:
        fp = get_working_dir('logs') / filename

        try:
            with open(fp, 'a', encoding="utf-8") as f:
                if header:
                    f.write(header + "\n")
                subprocess.run(command, check=True, stdout=f, stderr=subprocess.STDOUT)
            return True
        except subprocess.CalledProcessError as err:
            self.append(LogLevel.LOG_LEVEL_ERROR.value, f"Command failed {err}")
            return False
        except Exception as err:
            self.append(LogLevel.LOG_LEVEL_ERROR.value, f"Logging/proc error {err}")
            return False

def CORE_TRACE_LOG(level: int, message: str):
    logger = Log()
    logger.append(level, message)


if __name__ == '__main__':
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_ERROR.value, "test")
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_LOG.value, "motorku")
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_WARNING.value, "asaasas")
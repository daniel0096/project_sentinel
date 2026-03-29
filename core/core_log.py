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

@singletonclass
class Log:
    def __init__(self):
        self.log_files = log_files.get('log', [])

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
            fp = get_working_dir('logs') / target_file
            try:
                with open(fp, 'a', encoding="utf-8") as f:
                    f.write(f"[{timestamp}] {log_label}: {message}\n")
                    print(f"[{timestamp}] {log_label}: {message}")
                return True
            except Exception as err:
                print(f"Error while writing into log file. {err}")

        return False

def CORE_TRACE_LOG(level: int, message: str):
    logger = Log()
    logger.append(level, message)


if __name__ == '__main__':
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_ERROR.value, "test")
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_LOG.value, "motorku")
    CORE_TRACE_LOG(LogLevel.LOG_LEVEL_WARNING.value, "asaasas")
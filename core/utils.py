import os

PROJECT_DIR: str = os.getcwd()

def get_working_dir(directory: str) -> str:
    return os.path.join(PROJECT_DIR, directory)

if __name__ == '__main__':
    print(f"working dir: {get_working_dir('core')}")

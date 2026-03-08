import server
import sys
from utils import HELP_TEXT

def init():
    sv = server.Server()

    if len(sys.argv) < 2 or "--help" in sys.argv or "-h" in sys.argv:
        print(HELP_TEXT)
        return

    cmd = " ".join(sys.argv[1:])
    sv.run_cmd(cmd)

if __name__ == '__main__':
    init()
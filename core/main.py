import server

def init():
    sv = server.Server()
    sv.connect()

if __name__ == '__main__':
    init()
import socket

class Listener():

    def __init__(self,address,port):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((address, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
                    return data


class Sender():

    def __init__(self,address,port):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((address, port))
            s.sendall(b'Hello, world')
            data = s.recv(1024)

        print('Received', repr(data))

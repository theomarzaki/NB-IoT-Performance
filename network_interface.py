# This file acts as a network interface between the module and the 'edge' cloud

import socket

class Listener():

    # Intended as a server to obtain the TCP packets that the module sends for evaluation of performance

    def __init__(self,address,port):
        self.address = address
        self.port = port

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.address, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    print(data)
                    if not data:
                        break
                conn.sendall("Hello World !")
                print(data)


class Sender():

    # Sends the AT commands if the module is conncted from edge cloud

    def __init__(self,address,port):
        self.address = address
        self.port = port

    def send(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.address, self.port))
            s.sendall(b'AT')
            data = s.recv(1024)

        print('Received', repr(data))

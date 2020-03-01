import socket

HOST = 'localhost'
PORT = 12345

class Client:

    def __init__(self, nickname):

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.nickname = nickname

    def connect(self, addr):

        self.socket.connect(addr)

    def receive(self, sock):

        data = sock.recv(2048).decode("utf8")
        return data

    def send(self, sock, data):

        sock.send(bytes(data,'utf8'))

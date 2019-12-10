from threading import Thread
import socket

from logic.GameLogic import *

class Server:

    def __init__(self, port=10030):

        self.__socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	self.__host_ip = self.__socket.gethostbyname(self.__socket.gethostname())
	self.__port = port

    def waiting_for_connection(self):

        #

    def start(self):

        try:
            self.__socket.bind((HOST,PORT))
        except socket.error as e:
            print(str(e))

        self.__socket.listen(5)

        print("Server IP: " + self.__host_ip)
        print("waiting for connection...")
        Thread(target = waiting_for_connection).start()


class GameServer:

    def __init__(self, server):

        #

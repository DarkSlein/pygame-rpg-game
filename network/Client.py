import socket
import threading
import json

INFO_TIMEOUT = 10000

class Client:

    def __init__(self, address, scene):

        self.__signal = True
        self.__sendInfoMessages = False # если True, то отправляет info-сообщения
        self.__infoIterator = 0 # итератор для таймаута между info-запросами

        self.__id = -1 # значение присваивается, когда приходит connect-сообщение

        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect(address)

        except:
            print("Could not make a connection to the server")

        self.__receiveThread = threading.Thread(target = self.__receive)
        self.__receiveThread.start()

        # send "connect" to server
        self.send("connect")

    def update(self):

        self.__send_info_query()

    def send(self, message):

        self.__socket.sendall(str.encode(message))

    def get_id(self):

        return self.__id

    def __send_info_query(self):

        if not self.__sendInfoMessages:
            return

        if self.__infoIterator == INFO_TIMEOUT:
            self.send("info")
            self.__infoIterator = 0
        self.__infoIterator += 1

    def __receive(self):
        
        while self.__signal:
            
            try:
                data = self.__socket.recv(128)
                
            except:
                print("You have been disconnected from the server")
                self.__signal = False
                break

            print(data.decode("utf-8"))
            messageDict = json.loads(data.decode("utf-8").split("}")[0] + "}")

            messageType = messageDict["type"]
            
            if messageType == "connect":
                self.__id = messageDict["id"]
            elif messageType == "info":
                pass
                
            #print(str(entityDict["id"]) + " " + str(entityDict["x"]) + " " +
            #      str(entityDict["y"]) + " " + entityDict["status"] + " " +
            #      entityDict["direction"])

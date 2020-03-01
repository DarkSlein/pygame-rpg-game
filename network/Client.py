import socket
import threading
import json

from logic.Map import Map

INFO_TIMEOUT = 10000

class Client:

    def __init__(self, address, scene):

        self.__signal = True
        self.__sendInfoMessages = False # если True, то отправляет info-сообщения
        self.__infoIterator = 0 # итератор для таймаута между info-запросами

        self.__playerId = -1 # значение присваивается, когда приходит connect-сообщение
        self.__entities = {}

        self.__map = Map(32, 32)

        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect(address)

        except:
            print("Could not make a connection to the server")

        self.__receiveThread = threading.Thread(target = self.__receive)
        self.__receiveThread.start()

        self.send("connect")

    def update(self):

        self.__send_info_query()

    def send(self, message):

        self.__socket.sendall(str.encode(message))

    def get_player_id(self):

        return self.__playerId

    def get_entity(self, entityId):

        return self.__entities[entityId]

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
                self.__playerId = messageDict["player_id"]
                self.__sendInfoMessages = True
            elif messageType == "info":
                self.entities[entityId] = {"x": messageDict["x"],
                                           "y": messageDict["y"],
                                           "status": messageDict["status"],
                                           "direction": messageDict["direction"]}

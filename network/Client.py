import socket
import threading
import json

from logic.vectors import SquareVector, PixelVector

INFO_TIMEOUT = 5 #5 or 20
END_OF_MESSAGE = "|"

class Client:

    def __init__(self, address):

        self.__signal = True
        self.__sendInfoMessages = False # если True, то отправляет info-сообщения
        self.__infoIterator = 0 # итератор для таймаута между info-запросами

        self.__playerId = -1 # значение присваивается, когда приходит connect-сообщение
        self.__entities = {}

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

#        entitiesForDeletion = []

#        for entityId, entityDict in self.__entities.items():

#            if entityDict["status"] == "destroyed":
#                entitiesForDeletion.append(entityId)

#        for entityId in entitiesForDeletion:
#            del self.__entities[entityId]  

    def send(self, message):

        self.__socket.sendall(str.encode(message + END_OF_MESSAGE))

    def get_player_id(self):

        return self.__playerId

    def get_entity(self, entityId):

        if not entityId in self.__entities:
            return False

        return self.__entities[entityId]

    def get_object(self, posSquare):

        pass

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
                data = self.__socket.recv(2048) #128
                
            except:
                print("You have been disconnected from the server")
                self.__signal = False
                break

            #print(data.decode("utf-8"))

            dataSplited = data.decode("utf-8").split("}")

            for message in dataSplited:

                if message != "":
                    self.__reply(message + "}")
                
    def __reply(self, message):

        messageDict = json.loads(message)
        messageType = messageDict["type"]
            
        if messageType == "connect":
            self.__playerId = messageDict["player_id"]
            self.__sendInfoMessages = True
            
        elif messageType == "i": # info
            entityId = messageDict["e"]
            if not entityId in self.__entities:
                self.__entities[entityId] = {}
                
            self.__entities[entityId]["x"] = messageDict["x"]
            self.__entities[entityId]["y"] = messageDict["y"]
            self.__entities[entityId]["status"] = messageDict["s"]
            self.__entities[entityId]["direction"] = messageDict["d"]
            self.__entities[entityId]["objType"] = messageDict["o"]
            
        elif messageType == "ch": # character
            entityId = messageDict["e"]
            if not entityId in self.__entities:
                self.__entities[entityId] = {}

            self.__entities[entityId]["name"] = messageDict["n"]

        elif messageType == "d":
            entityId = messageDict["e"]
            if entityId in self.__entities:
                del self.__entities[entityId]

    def get_entities_dict(self):

        return self.__entities.copy()

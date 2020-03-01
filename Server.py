import socket
import threading
import json

from time import sleep

from logic.GameLogic import GameLogic
from logic.entities.Character import Character
from logic.vectors import SquareVector, PixelVector

LOOP_DELAY = 1/240 #1/60
END_OF_MESSAGE = "|"

class Server:

    def __init__(self):

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__totalConnections = 0
        self.__connections = []
        self.logic = GameLogic()
        self.logic.create_map()

    def start(self, address):

        self.__socket.bind(address)
        self.__socket.listen(5)

        self.__waitForConnectionsThread = threading.Thread(
            target = self.wait_for_connections)
        self.__waitForConnectionsThread.start()

        print("Server started...")

        while True:
            
            self.update()
            sleep(LOOP_DELAY)

    def wait_for_connections(self):

        while True:

            clientSock, clientAddress = self.__socket.accept()
            
            clientId = len(self.__connections)
            self.__connections.append(ClientHandler(clientSock, clientAddress,
                                                    clientId, self))

            print("New connection at ID " + str(clientId))
            self.__connections[clientId].start()
            self.__totalConnections += 1

    def get_connections(self):

        return self.__connections

    def update(self):

        self.logic.update()

class ClientHandler(threading.Thread):

    def __init__(self, socket, address, clientId, server):

        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.clientId = clientId
        self.server = server
        self.signal = True
        self.playerId = -1

    def run(self):

        while self.signal:

            try:
                data = self.socket.recv(32)
 
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                self.server.get_connections().remove(self)
                break

            if data != "" and data.decode("utf-8") != "":

                dataSplited = data.decode("utf-8").split(END_OF_MESSAGE)

                for message in dataSplited:

                    if message != "":

#                        if message != "info": 
#                            print("ID " + str(self.clientId) + ": " +
#                                  str(message))
                        self.__on_command(message)

    def __on_command(self, command):

        if command == "info":
            self.__send_info()
        elif command == "connect":
            self.__create_player()

        if self.playerId == -1: # TODO: exception
            return

        if command == "walking" or command == "standing":
            self.server.logic.get_entity(self.playerId).set_action(command)
        elif command == "right" or command == "left" or \
        command == "down" or command == "up":
            self.server.logic.get_entity(self.playerId).set_direction(command)

    def __send(self, messageDict):

        messageJson = json.dumps(messageDict)
        self.socket.sendall(messageJson.encode())

    def __send_info(self):

        for entityId, entity in enumerate(self.server.logic.map.entities):

            entityPos = entity.get_position()
            
            if issubclass(type(entity), Character): # TODO: fix kostyl
                name = entity.get_name()
            else:
                name = ""

            messageDict = {"type": "info", # maybe types: player, npc, projectile
                           "entity_id": entityId,
                           "x": entityPos.x,
                           "y": entityPos.y,
                           "status": entity.get_action(),
                           "direction": entity.get_direction(),
                           "name": name}
            self.__send(messageDict)

    def __create_player(self):

        self.playerId = self.server.logic.add_player(PixelVector(100,100))
        print("Player created...")

        self.__send_player_id()

    def __send_player_id(self):

        messageDict = {"type": "connect",
                       "player_id": self.playerId}
        self.__send(messageDict)

        print("Player ID " + str(self.playerId) + " is send to client " +
              str(self.clientId) + "...")

if __name__ == '__main__':

    server = Server()
    server.start(("localhost", 666))

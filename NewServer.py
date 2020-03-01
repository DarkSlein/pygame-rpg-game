import socket
import threading
import json

from time import sleep

from logic.GameLogic import GameLogic

class Server:

    def __init__(self):

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__totalConnections = 0
        self.__connections = []
        self.__logic = GameLogic()
        self.__logic.create_map()

    def start(self, address):

        self.__socket.bind(address)
        self.__socket.listen(5)

        self.__waitForConnectionsThread = threading.Thread(
            target = self.wait_for_connections)
        self.__waitForConnectionsThread.start()

        print("Server started...")

        while True:
            
            self.update()
            sleep(1/60)

    def wait_for_connections(self):

        while True:

            clientSock, clientAddress = self.__socket.accept()
            
            identificator = self.__totalConnections
            self.connections.append(ClientHandler(clientSock, clientAddress,
                                                  identificator, self))

            self.__connections[identificator].start()
            print("New connection at ID " + str(identificator))
            self.__totalConnections += 1

    def update(self):

        self.__logic.update()

class ClientHandler(threading.Thread):

    def __init__(self, socket, address, identificator, server):

        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = identificator
        self.server = server
        self.signal = True

    def run(self):

        while self.signal:

            try:
                data = self.socket.recv(32)
 
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                self.server.connections.remove(self)
                break

            if data != "" and data.decode("utf-8") != "":
                if data.decode("utf-8") != "info":
                    print("ID " + str(self.id) + ": " + str(data.decode("utf-8")))
                self.__on_command(data.decode("utf-8"))

    def __on_command(self, command):

        if command == "walking" or command == "standing":
            #self.server.players[self.id].status = command
        elif command == "right" or command == "left" or \
        command == "down" or command == "up":
            #self.server.players[self.id].direction = command
        elif command == "info":
            self.__send_info()
        elif command == "connect":
            self.__create_player()

    def __send(self, messageDict):

        messageJson = json.dumps(messageDict.encode())
        self.socket.sendall(messageJson.encode())

    def __send_info(self):

        for entityId, entity in self.__logic.map.entities:

            entityPos = entity.get_position()
            messageDict = {"type": "info",
                           "entity_id": entityId,
                           "x": entityPos.x,
                           "y": entityPos.y}
            self.__send(messageDict)

    def __create_player(self):

        self.__process.logic.add_player(PLAYER_NAME, PixelVector(100,100))

        self.__send_player_id(playerId)

    def __send_player_id(self, playerId):

        messageDict = {"type": "connect",
                       "id": playerId}
        self.__send(messageDict)

if __name__ == '__main__':

    server = Server()
    server.start(("localhost", 666))

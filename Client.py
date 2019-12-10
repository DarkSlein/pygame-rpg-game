import pygame
import socket

from logic.GameLogic import *
from graphics.Menu import *
from network.package import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
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
        
class Game:

    def __init__(self, client=None):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.game = GameLogic()
        self.menu = Menu(self.screen)
#        self.player = self.game.add_player("player")
        self.client = client

    def render(self):
        pass

    def loop(self):

        while self.running:
            self.handle_events()
            self.render()

        
if __name__ == '__main__':
#    nickname = input('Enter your nickname: ')
#    client = Client(nickname)
#    client.connect((HOST, PORT))

    game = Game()
    game.loop()
    pygame.quit()

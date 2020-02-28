import pygame

from logic.GameLogic import *
from scenes.Menu import *
from scenes.SingleplayerGame import *
from scenes.MultiplayerGame import *
from network.package import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

class Process:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.logic = False
        #self.logic = GameLogic() # or GameLogicClient(self) and GameLogicServer(self)

        self.menu = Menu(self)
        self.game = False #SingleGame(self)
        self.soundVolume = 100
        self.currentScene = self.menu

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.currentScene.on_event(event)


    def loop(self):

        while self.running:

            self.handle_events()
            self.currentScene.update()

            if self.logic:
                self.logic.update()

    def quit(self):

        self.running = False

    def change_scene(self, scene):

        self.currentScene = scene

    def init_logic(self):

        self.logic = GameLogic()

    def init_game(self, gameType):

        if gameType == "singleplayer":
            self.game = SingleplayerGame(self)
        elif gameType == "multiplayer":
            self.game = MultiplayerGame(self)

        
if __name__ == '__main__':
#    nickname = input('Enter your nickname: ')
#    client = Client(nickname)
#    client.connect((HOST, PORT))

    main = Process()
    main.loop()
    pygame.quit()

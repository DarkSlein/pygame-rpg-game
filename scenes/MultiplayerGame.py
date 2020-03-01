import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from network.Client import Client
from logic.vectors import SquareVector, PixelVector

class MultiplayerGame(Scene):

    def __init__(self, process):

        self.__process = process
        self.camera = Camera(0,0,self)
        self.client = Client(("localhost", 666), self)

        self.tiles = pygame.image.load("assets/tiles.png").convert()
        self.charactersTiles = {
            "player": pygame.image.load("assets/player.png").convert_alpha(),
            "player2": pygame.image.load("assets/player2.png").convert_alpha()
            }

        self.entities = {}

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__process.change_scene(self.__process.menu)
            elif event.key == pygame.K_DOWN:
                self.client.send("walking")
                self.client.send("down")
            elif event.key == pygame.K_UP:
                self.client.send("walking")
                self.client.send("up")
            elif event.key == pygame.K_RIGHT:
                self.client.send("walking")
                self.client.send("right")
            elif event.key == pygame.K_LEFT:
                self.client.send("walking")
                self.client.send("left")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
               or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.client.send("standing")

    def update(self):

        self.client.update()
        self.render()

    def render(self):

        self.render_bg()
        self.render_sprites()

        self.camera.update(0)

        pygame.display.flip()


    def render_bg(self):

        pass

    def render_sprites(self):

        pass

    def get_player_position(self):

        playerId = self.client.get_player_id()
        player = self.client.get_entity(playerId)

        return PixelVector(player["x"], player["y"])

import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from network.Client import Client
from logic.vectors import SquareVector, PixelVector

from logic.entities.Fireball import Fireball

PLAYER_NAME = "player1" # TODO: custom names

class MultiplayerGame(Scene):

    def __init__(self, process):

        self.__process = process
        self.camera = Camera(0,0,self)

        self.__process.logic.create_map(480,640) # TODO: fix kostyl
        self.tiles = pygame.image.load("assets/tiles.png").convert()
        self.charactersTiles = {
            "player": pygame.image.load("assets/player.png").convert_alpha(),
            "player2": pygame.image.load("assets/player2.png").convert_alpha(),
            "fireball": pygame.image.load("assets/fireball.png").convert_alpha()
            }

        self.entities = {}

    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__process.change_scene(self.__process.menu)
            elif event.key == pygame.K_DOWN:
                self.__process.client.send("walking")
                self.__process.client.send("down")
            elif event.key == pygame.K_UP:
                self.__process.client.send("walking")
                self.__process.client.send("up")
            elif event.key == pygame.K_RIGHT:
                self.__process.client.send("walking")
                self.__process.client.send("right")
            elif event.key == pygame.K_LEFT:
                self.__process.client.send("walking")
                self.__process.client.send("left")
            elif event.key == pygame.K_SPACE:
                self.__process.client.send("cast")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
               or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.__process.client.send("standing")

    def update(self):

        self.render()

    def render(self):

        self.render_bg()
        self.render_sprites()

        self.camera.update(0)

        pygame.display.flip()


    def render_bg(self):

        start_col = int(self.camera.x // 64)
        start_row = int(self.camera.y // 64)

        # draw map
        for i in range(start_row, start_row + 11):
            for j in range(start_col, start_col + 14):

                if j < 20 and i < 20:
                    obj = self.__process.logic.get_object(SquareVector(i, j))
                    texture = self.tiles.subsurface(obj.j*64,obj.i*64,64,64)
                    self.__process.screen.blit(texture,(j*64 - self.camera.x,
                                                        i*64 - self.camera.y))

    def render_sprites(self):

        client = self.__process.client
        for entityId, entityDict in client.get_entities_dict().items():

            # TODO: different skins by name
            if entityDict["objType"] == "p": # player
                sprite = self.charactersTiles["player"].subsurface(0*64,2*64,64,64)
            elif "name" in entityDict and entityDict["name"] == "npc_test": # TODO: dirty hack
                sprite = self.charactersTiles["player2"].subsurface(0*64,2*64,64,64)
            elif entityDict["objType"] == "f": # fireball
                sprite = self.charactersTiles["fireball"].subsurface(0*64,0*64,64,64)
            else:
                sprite = self.charactersTiles["player2"].subsurface(0*64,2*64,64,64)

            pos = PixelVector(entityDict["x"], entityDict["y"])
            self.__process.screen.blit(sprite,(pos.x - self.camera.x,
                                               pos.y - self.camera.y))

    def get_player_position(self):

        playerId = self.__process.client.get_player_id()
        player = self.__process.client.get_entity(playerId)

        if not player:
            return PixelVector(0, 0)

        return PixelVector(player["x"], player["y"])

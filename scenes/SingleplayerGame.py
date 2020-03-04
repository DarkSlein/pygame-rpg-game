import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from logic.Map import Map
from logic.vectors import SquareVector, PixelVector

from logic.entities.Character import Character
from logic.entities.Fireball import Fireball

PLAYER_NAME = "player1"

class SingleplayerGame(Scene):

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
        self.playerId = self.__process.logic.add_player(PixelVector(100,100),
                                                        name=PLAYER_NAME)


    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__process.change_scene(self.__process.menu)
            elif event.key == pygame.K_DOWN:
                self.__get_player().set_direction("down")
                self.__get_player().set_action("walking")
            elif event.key == pygame.K_UP:
                self.__get_player().set_direction("up")
                self.__get_player().set_action("walking")
            elif event.key == pygame.K_RIGHT:
                self.__get_player().set_direction("right")
                self.__get_player().set_action("walking")
            elif event.key == pygame.K_LEFT:
                self.__get_player().set_direction("left")
                self.__get_player().set_action("walking")
            elif event.key == pygame.K_SPACE:
                self.__get_player().cast()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
               or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.__get_player().set_action("standing")

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

        logic = self.__process.logic
        for entityId, entity in logic.get_entities().items():

            if issubclass(type(entity), Character):
                if entity.get_name() == PLAYER_NAME:
                    sprite = self.charactersTiles["player"].subsurface(0*64,2*64,64,64)
                elif entity.get_name() == "npc_test":
                    sprite = self.charactersTiles["player2"].subsurface(0*64,2*64,64,64)
                else:
                    sprite = self.charactersTiles["player"].subsurface(0*64,2*64,64,64)

            elif issubclass(type(entity), Fireball):
                sprite = self.charactersTiles["fireball"]

            pos = entity.get_position()
            self.__process.screen.blit(sprite,(pos.x - self.camera.x,
                                               pos.y - self.camera.y))

    def __get_player(self):

        return self.__process.logic.get_entity(self.playerId)

    def get_player_position(self): # for camera, universal method for single and multi

        return self.__get_player().get_position()

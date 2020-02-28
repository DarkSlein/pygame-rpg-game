import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from logic.Map import Map
from logic.vectors import SquareVector, PixelVector

PLAYER_NAME = "player1"

class SingleplayerGame(Scene):

    def __init__(self, process):
        
        self.__process = process
        self.camera = Camera(0,0,self)

        self.__process.logic.create_map(480,640)
        self.map = self.__process.logic.map
        self.tiles = pygame.image.load("assets/tiles.png").convert()
        self.charactersTiles = {
            "player": pygame.image.load("assets/player.png").convert_alpha(),
            "player2": pygame.image.load("assets/player2.png").convert_alpha()
            }
        self.player = self.__process.logic.add_player(PLAYER_NAME,
                                                      PixelVector(100,100))


    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__process.change_scene(self.__process.menu)
            elif event.key == pygame.K_DOWN:
                self.player.set_direction("down")
                self.player.set_action("walking")
#                self.camera.y += 10
            elif event.key == pygame.K_UP:
                self.player.set_direction("up")
                self.player.set_action("walking")
#                self.camera.y -= 10
            elif event.key == pygame.K_RIGHT:
                self.player.set_direction("right")
                self.player.set_action("walking")
#                self.camera.x += 10
            elif event.key == pygame.K_LEFT:
                self.player.set_direction("left")
                self.player.set_action("walking")
#                self.camera.x -= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
               or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.player.set_action("standing")

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
                    obj = self.__process.logic.objects[self.map.grid[i][j]]
                    sprite = self.tiles.subsurface(obj.j*64,obj.i*64,64,64)
                    self.__process.screen.blit(sprite,(j*64 - self.camera.x,
                                                       i*64 - self.camera.y))

    def render_sprites(self):

#        self.player.update()

        for identificator, entity in self.map.entities.items():

            if identificator == PLAYER_NAME:
                sprite = self.charactersTiles["player"].subsurface(0*64,2*64,64,64)
            elif identificator == "npc_test":
                sprite = self.charactersTiles["player2"].subsurface(0*64,2*64,64,64)
            pos = entity.get_position()
            self.__process.screen.blit(sprite,(pos.x - self.camera.x,
                                               pos.y - self.camera.y))

    def get_player_position(self):

        return self.player.get_position()

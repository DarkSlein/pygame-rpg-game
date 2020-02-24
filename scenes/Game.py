import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from logic.Map import Map
from logic.vectors import SquareVector, PixelVector

PLAYER_NAME = "player1"

class Game(Scene):

    def __init__(self, process):
        
        self.__process = process
#        self.player = self.__process.logic.add_player("player")
#        print(self.player.get_position())
        self.camera = Camera(0,0,self)
        self.__process.logic.create_map(480, 640)
        self.map = self.__process.logic.map
        self.tiles = pygame.image.load("assets/tiles.png").convert()
        self.playerTiles = pygame.image.load("assets/player.png").convert_alpha()
#        self.objects = [
#            GameObject(0,0,walkable=True,shootable=True), # 0 - grass
#            GameObject(0,1,walkable=False,shootable=False), # 1 - stone
#            GameObject(0,2,walkable=True,shootable=True), # 2 - plant
#            GameObject(0,3,walkable=False,shootable=True), # 3 - tree
#            GameObject(0,4,walkable=True,shootable=True), # 4 - flowers
#            GameObject(0,5,walkable=False,shootable=False), # 5 - wall
#            GameObject(0,6,walkable=False,shootable=False), # 6 - top wall
#            GameObject(0,7,walkable=False,shootable=False), # 7 - top wall with r end
#            GameObject(0,8,walkable=False,shootable=False), # 8 - top wall with l end
#            GameObject(0,9,walkable=False,shootable=False), # 9 - wall with r end
#            GameObject(1,5,walkable=False,shootable=False), # 10 - bottom-wall
#            GameObject(1,6,walkable=False,shootable=False), # 11 - bottom-wall with r-end
#            GameObject(1,7,walkable=False,shootable=False), # 12 - bottom-wall with l-end
#            GameObject(1,8,walkable=False,shootable=False), # 13 - wall with l end
#            GameObject(1,9,walkable=True,shootable=True), # 14 - top-grass with l-end
#            GameObject(2,9,walkable=True,shootable=True), # 15 - top-grass with r-end
#            GameObject(2,8,walkable=True,shootable=True), # 16 - stairs
#            GameObject(1,0,walkable=True,shootable=True),
#            GameObject(1,1,walkable=True,shootable=True),
#            GameObject(1,2,walkable=True,shootable=True),
#            GameObject(2,0,walkable=True,shootable=True),
#            GameObject(2,1,walkable=True,shootable=True),
#            GameObject(2,2,walkable=True,shootable=True),
#            GameObject(3,0,walkable=True,shootable=True),
#            GameObject(3,1,walkable=True,shootable=True),
#            GameObject(3,2,walkable=True,shootable=True),
#            GameObject(1,3,walkable=True,shootable=True),
#            GameObject(1,4,walkable=True,shootable=True),
#            GameObject(2,3,walkable=True,shootable=True),
#            GameObject(2,4,walkable=True,shootable=True)
#            ]
        self.player = self.__process.logic.add_player(PLAYER_NAME, PixelVector(100, 100))


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

            sprite = self.playerTiles.subsurface(0*64,2*64,64,64)
            pos = entity.get_position()
            self.__process.screen.blit(sprite,(pos.x - self.camera.x,
                                               pos.y - self.camera.y))

        pass

    def on_press(self, keyEvent):

#        if self.__state == "menu":
#            if event.key == pygame.K_DOWN:
#                self.menu.
#            if event.key == pygame.K_UP:    
                
#        elif self.__state == "game":
            pass

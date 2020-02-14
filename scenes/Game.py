import pygame

from scenes.Scene import Scene
from scenes.Camera import Camera
from logic.objects.GameObject import GameObject

class Game(Scene):

    def __init__(self, process):
        
        self.__process = process
        self.player = self.__process.logic.add_player("player")
        self.camera = Camera(0,0,self)
        self.map = [
            [3 ,20,22,3 ,3 ,3 ,3 ,1 ,1 ,3 ,3 ,14,3 ,0 ,3 ,3 ,0 ,3 ,15,3],
	    [3 ,20,22,3 ,3 ,0 ,1 ,17,19,1 ,3 ,14,17,18,18,18,18,19,15,3],
            [3 ,20,22,3 ,3 ,0 ,0 ,20,22,0 ,3 ,14,23,24,24,24,24,25,15,3],
            [3 ,20,22,3 ,0 ,0 ,1 ,23,25,1 ,3 ,8 ,6 ,6 ,6 ,6 ,16,6 ,7 ,3],
            [3 ,20,22,0 ,0 ,3 ,3 ,1 ,1 ,3 ,3 ,13,5 ,5 ,5 ,5 ,16,5 ,9 ,3],
            [3 ,20,22,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,12,10,10,10,10,16,10,11,3],
            [3 ,20,22,3 ,3 ,2 ,0 ,2 ,0 ,3 ,3 ,0 ,2 ,0 ,4 ,0 ,0 ,0 ,2 ,3],
            [3 ,20,28,18,18,18,18,18,18,18,18,18,18,18,18,18,18,19,0 ,3],
            [3 ,23,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,25,3 ,3],
            [3 ,2 ,3 ,3 ,3 ,3 ,3 ,3 ,2 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,0 ,3 ,3 ,3],
            [3 ,0 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,3 ,17,18,18,19,0 ,0 ,2 ,0 ,0 ,1],
            [3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,0 ,3 ,20,26,27,22,2 ,3 ,0 ,0 ,1 ,3],
            [3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,20,28,29,22,0 ,0 ,3 ,0 ,0 ,3],
            [3 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,23,24,24,25,0 ,2 ,0 ,0 ,4 ,3],
            [3 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,1 ,0 ,3],
            [3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,3 ,0 ,0 ,0 ,1],
            [3 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,2 ,2 ,0 ,1 ,0 ,0 ,0 ,2 ,0 ,1],
            [3 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,17,18,18,18,18,18,18,18],
            [3 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,23,24,24,24,24,24,24,24],
            [3 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        ]
        #self.map = self.__process.logic.map
        self.tiles = pygame.image.load("assets/tiles.png").convert()
        self.objects = [
            GameObject(0,0,walkable=True,shootable=True), # 0 - grass
            GameObject(0,1,walkable=False,shootable=False), # 1 - stone
            GameObject(0,2,walkable=True,shootable=True), # 2 - plant
            GameObject(0,3,walkable=False,shootable=True), # 3 - tree
            GameObject(0,4,walkable=True,shootable=True), # 4 - flowers
            GameObject(0,5,walkable=False,shootable=False), # 5 - wall
            GameObject(0,6,walkable=False,shootable=False), # 6 - top wall
            GameObject(0,7,walkable=False,shootable=False), # 7 - top wall with r end
            GameObject(0,8,walkable=False,shootable=False), # 8 - top wall with l end
            GameObject(0,9,walkable=False,shootable=False), # 9 - wall with r end
            GameObject(1,5,walkable=False,shootable=False), # 10 - bottom-wall
            GameObject(1,6,walkable=False,shootable=False), # 11 - bottom-wall with r-end
            GameObject(1,7,walkable=False,shootable=False), # 12 - bottom-wall with l-end
            GameObject(1,8,walkable=False,shootable=False), # 13 - wall with l end
            GameObject(1,9,walkable=True,shootable=True), # 14 - top-grass with l-end
            GameObject(2,9,walkable=True,shootable=True), # 15 - top-grass with r-end
            GameObject(2,8,walkable=True,shootable=True), # 16 - stairs
            GameObject(1,0,walkable=True,shootable=True),
            GameObject(1,1,walkable=True,shootable=True),
            GameObject(1,2,walkable=True,shootable=True),
            GameObject(2,0,walkable=True,shootable=True),
            GameObject(2,1,walkable=True,shootable=True),
            GameObject(2,2,walkable=True,shootable=True),
            GameObject(3,0,walkable=True,shootable=True),
            GameObject(3,1,walkable=True,shootable=True),
            GameObject(3,2,walkable=True,shootable=True),
            GameObject(1,3,walkable=True,shootable=True),
            GameObject(1,4,walkable=True,shootable=True),
            GameObject(2,3,walkable=True,shootable=True),
            GameObject(2,4,walkable=True,shootable=True)
            ]


    def on_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__process.change_scene(self.__process.menu)
            elif event.key == pygame.K_DOWN:
                self.camera.y += 10
            elif event.key == pygame.K_UP:
                self.camera.y -= 10
            elif event.key == pygame.K_RIGHT:
                self.camera.x += 10
            elif event.key == pygame.K_LEFT:
                self.camera.x -= 10

    def render(self):

        self.render_bg()

        self.camera.update(0)

        pygame.display.flip()

    def render_bg(self):

        start_col = self.camera.x // 64
        start_row = self.camera.y // 64

        print(start_col, start_row)

        # draw map
        for i in range(start_row, start_row + 11):
            for j in range(start_col, start_col + 22):
                if j < 20 and i < 20:
                    obj = self.objects[self.map[i][j]]
                    sprite = self.tiles.subsurface(obj.j*64,obj.i*64,64,64)
                    self.__process.screen.blit(sprite,(j*64 - self.camera.x,
                                                       i*64 - self.camera.y))


    def on_press(self, keyEvent):

#        if self.__state == "menu":
#            if event.key == pygame.K_DOWN:
#                self.menu.
#            if event.key == pygame.K_UP:    
                
#        elif self.__state == "game":
            pass

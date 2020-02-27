import time

from logic.Map import Map
from logic.AI import AI
from logic.entities.Player import Player
from logic.entities.Npc import Npc
from logic.objects.GameObject import GameObject
from logic.vectors import SquareVector, PixelVector

FPS = 60
loopDelay = 1/FPS

class GameLogic:

        def __init__(self):

                self.map = False
                self.active = True # TODO: when pause then active is False
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
                    GameObject(1,0,walkable=True,shootable=True), # 17
                    GameObject(1,1,walkable=True,shootable=True), # 18
                    GameObject(1,2,walkable=True,shootable=True), # 19
                    GameObject(2,0,walkable=True,shootable=True), # 20
                    GameObject(2,1,walkable=True,shootable=True), # 21
                    GameObject(2,2,walkable=True,shootable=True), # 22
                    GameObject(3,0,walkable=True,shootable=True),
                    GameObject(3,1,walkable=True,shootable=True),
                    GameObject(3,2,walkable=True,shootable=True),
                    GameObject(1,3,walkable=True,shootable=True),
                    GameObject(1,4,walkable=True,shootable=True),
                    GameObject(2,3,walkable=True,shootable=True),
                    GameObject(2,4,walkable=True,shootable=True)
                    ]
                self.__state = "game"
                self.__ai = AI(self)

        def create_map(self, x=32, y=32):

                self.map = Map(x, y)
                self.add_entity("npc_test", Npc(PixelVector(400, 500), speed=0.1))

        def load_map(self):

                pass

        def save_map(self):

                pass

        def is_map_loaded(self):

                if not self.map: # map isn't loaded
                        return False
                return True

        def get_entity(self, identificator):
                
                return self.map.get_entity(identificator)

        def get_object(posSquare):

#                if not self.map: # map isn't loaded
#                        return False

                return self.map.get_object(posSquare)

        def add_entity(self, identificator, entity):

#                if not self.map: # map isn't loaded
#                        return False

                return self.map.add_entity(identificator, entity)

        def add_player(self, identificator, posPixel):

                player = Player(posPixel, 0.5, "down")
                return self.add_entity(identificator, player)

        def move_entity(self, entity, radius):

                return self.map.move_entity(entity, radius)

        def is_obstacle(self, posPixel):

                posPixel.x += 20
                posPixel.y += 20
                posSquare1 = posPixel.to_square()
                
                posPixel.x += 26
                posPixel.y += 36
                posSquare2 = posPixel.to_square()
                
                objNum1 = self.map.grid[posSquare1.y][posSquare1.x]
                objNum2 = self.map.grid[posSquare2.y][posSquare2.x]
                #print(self.objects[objNum1].walkable,
                #      self.map.grid[posSquare1.y][posSquare1.x],
                #      posSquare1.x, posSquare1.y,
                #      self.map.grid[posSquare2.y + 1][posSquare2.x],
                #      posSquare2.x, posSquare2.y)
                result = not self.objects[objNum1].walkable or not self.objects[objNum2].walkable
                return result

        def __get_next_position(self, entity):

                pos = entity.get_position()

                if entity.get_direction() == "left":
                        nextPos = PixelVector(
                                pos.x - 5*entity.get_speed(), pos.y)
                elif entity.get_direction() == "right":
                        nextPos = PixelVector(
                                pos.x + 5*entity.get_speed(), pos.y)
                elif entity.get_direction() == "up":
                        nextPos = PixelVector(
                                pos.x, pos.y - 5*entity.get_speed())
                elif entity.get_direction() == "down":
                        nextPos = PixelVector(
                                pos.x, pos.y + 5*entity.get_speed())
                else:
                        pass # TODO: exception BadDirection
                
                return nextPos

        def update(self):

                for identificator, entity in self.map.entities.items():
                        
                        entity.update()
                        
                        if type(entity) is Npc:
                                self.__ai.control(entity)
                                
                        if entity.get_action() == "walking":
                                pos = self.__get_next_position(entity)
                                if not self.is_obstacle(pos):
                                        self.move_entity(entity, 5)
                                        entity.set_got_obstacle(False)
                                else:
                                        entity.set_got_obstacle(True)
                           

                self.map.update()

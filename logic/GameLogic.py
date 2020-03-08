import time

from logic.Map import Map
from logic.AI import AI
from logic.entities.Player import Player
from logic.entities.Npc import Npc
from logic.objects.GameObject import GameObject
from logic.vectors import SquareVector, PixelVector
#from logic.functions import *

FPS = 60
loopDelay = 1/FPS

class GameLogic:

        def __init__(self, mode=False):

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
                self.__mode = mode
                self.__deletedEntitiesIds = []

        def create_map(self, x=32, y=32):

                self.map = Map(x, y)
                self.add_entity(Npc(self.map, PixelVector(400, 500),
                                    speed=0.2, name="npc_test"))

        def load_map(self):

                pass

        def save_map(self):

                pass

        def is_map_loaded(self):

                if not self.map: # map isn't loaded
                        return False
                return True

        def get_entity(self, entityId):
                
                return self.map.get_entity(entityId)

        def get_object(self, posSquare):

#                if not self.map: # map isn't loaded
#                        return False

                return self.objects[self.map.get_object_id(posSquare)]

        def add_entity(self, entity):

#                if not self.map: # map isn't loaded
#                        return False

                return self.map.add_entity(entity)

        def add_player(self, posPixel, name="tester"):

                player = Player(self.map, posPixel, 0.5, "down", name)

                return self.add_entity(player)

        def move_entity(self, entityId, radius):

                return self.map.move_entity(entityId, radius)

        def is_obstacle(self, posPixel, currentEntity=None):

                isEntity = self.is_entity_obstacle(posPixel, currentEntity)
                isObject = self.is_object_obstacle(posPixel)

                return isEntity or isObject

        def is_entity_obstacle(self, posPixel, currentEntity=None):

                entityObstacle = False

                for entityId, entity in self.get_entities().items():

                        if currentEntity and entity == currentEntity:
                                continue

                        charPos = entity.get_position()
                        if (int(posPixel.x) in range(charPos.x - 20, # TODO: character.x + character.sizeX
                                                charPos.x + 20) and \
                            int(posPixel.y) in range(charPos.y - 32,
                                                charPos.y + 32)):
                                entityObstacle = entity

                return entityObstacle

        def is_object_obstacle(self, posPixel, shooting=False):

                posPixel.x += 20
                posPixel.y += 20
                posSquare1 = posPixel.to_square()
                
                posPixel.x += 26
                posPixel.y += 36
                posSquare2 = posPixel.to_square()
                
                objNum1 = self.map.grid[posSquare1.y][posSquare1.x]
                objNum2 = self.map.grid[posSquare2.y][posSquare2.x]

                if not shooting:
                        isObject = not self.objects[objNum1].walkable or \
                        not self.objects[objNum2].walkable
                else:
                        isObject = not self.objects[objNum1].shootable or \
                        not self.objects[objNum2].shootable

                return isObject

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

                entitiesForDeletion = []

                for entityId, entity in self.get_entities().items():
                        
                        entity.update()

                        if entity.get_action() == "walking" or \
                           entity.get_action() == "flying":
                                pos = self.__get_next_position(entity)
                                entityObstacle = self.is_entity_obstacle(pos,
                                                                         entity)
                                isObject = self.is_object_obstacle(pos)
                                if isObject:
                                        entity.set_got_obstacle(True)
                                        entity.on_obstacle()
                                elif entityObstacle and \
                                     entityObstacle.get_action() != "dead":
                                        entity.set_got_obstacle(True)
                                        entity.on_obstacle(entityObstacle)
                                else:
                                        self.move_entity(entityId, 5)
                                        entity.set_got_obstacle(False)

                        elif entity.get_action() == "destroyed":
                                entitiesForDeletion.append(entityId)

                for entityId in entitiesForDeletion:
                        del self.map.get_entities()[entityId]
                        if self.__mode == "server":
                                self.__deletedEntitiesIds.append(entityId)

                self.map.update()

        def get_entities(self):

                return self.map.get_entities().copy()

        def get_deleted_entities(self): # for multiplayer clients

                return self.__deletedEntitiesIds

        def clear_deleted_entities(self):

                self.__deletedEntitiesIds.clear()

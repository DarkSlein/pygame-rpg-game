#import MapObj
from logic.SquareVector import SquareVector
from logic.objects.Background import Background # objects -> blocks

import logic.objects
import logic.entities

class Map:

    def __init__(self, weight, height):

        self.__weight = weight
        self.__height = height
        self.__grid = [[0 for x in range(weight)] for y in range(height)]
        self.__entities = {}
        self.__objects = [Background]

    def is_obstacle(self, posSquare):
        
        return self.__grid[posSquare.x][posSquare.y].walkable

    def get_entity(self, identificator):

        return self.__entities[identificator]

    def get_object(self, posSquare): # TODO: exception throwing

        return self.__objects[self.__grid[posSquare.x][posSquare.y]];

#    def move_entity(self, identificator, direction, radius):

    def set_entity_position(self, identificator, posPixel):

        entity = get_entity(self, identificator)
        
        if entity.get_position().x > self.__weight:
            entity.set_position(self.__weight, entity.get_position().y)
        elif entity.get_position().x < 0:
            entity.set_position(0, entity.get_position().y)
        elif entity.get_position().y > self.__height:
            entity.set_position(entity.get_position().x, self.__height)
        elif entity.get_position().y < 0:
            entity.set_position(entity.get_position().x, 0)

        return entity.set_position(posPixel)

    def move_entity(self, identificator, direction, radius): # TODO: do something

        entity = get_entity(self, identificator)
        
        if entity.get_position().x > self.__weight:
            return entity.set_position(self.__weight, entity.get_position().y)
        elif entity.get_position().x < 0:
            return entity.set_position(0, entity.get_position().y)
        elif entity.get_position().y > self.__height:
            return entity.set_position(entity.get_position().x, self.__height)
        elif entity.get_position().y < 0:
            return entity.set_position(entity.get_position().x, 0)
        else:
            return entity.move(direction, radius)

    def object_exists(self, posSquare): # TODO: exception throwing

        return self.__grid[posSquare.x][posSquare.y] is not 0

    def entity_exists(self, identificator):

        return identificator in self.__entities

    def add_object(self, posSquare, objType): # TODO: exception throwing

        self.__grid[posSquare.x][posSquare.y] = objType


    def add_entity(self, identificator, entity):

        self.__entities[identificator] = entity

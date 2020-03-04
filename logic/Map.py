#import MapObj
from logic.objects.Background import Background # objects -> blocks
from logic.vectors import SquareVector, PixelVector

import logic.objects
import logic.entities

class Map:

    def __init__(self, weight, height):

        self.__weight = weight
        self.__height = height
        #self.grid = [[0 for x in range(weight)] for y in range(height)]
        self.grid = [
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
        self.entities = {}
        self.__entityIds = 0
        self.__projectiles = []
        self.__objects = [Background]

#    def is_obstacle(self, posSquare):
        
#        return self.grid[posSquare.x][posSquare.y].walkable

    def get_entity(self, entityId):

        return self.entities[entityId]

    def get_object_id(self, posSquare): # TODO: exception throwing

        return self.grid[posSquare.x][posSquare.y]

#    def move_entity(self, identificator, direction, radius):

    def set_entity_position(self, entityId, posPixel):

        entity = get_entity(self, entityId)
        
        if entity.get_position().x > self.__weight:
            entity.set_position(self.__weight, entity.get_position().y)
        elif entity.get_position().x < 0:
            entity.set_position(0, entity.get_position().y)
        elif entity.get_position().y > self.__height:
            entity.set_position(entity.get_position().x, self.__height)
        elif entity.get_position().y < 0:
            entity.set_position(entity.get_position().x, 0)

        return entity.set_position(posPixel)

    def move_entity(self, entityId, radius): # TODO: do something

        entity = self.get_entity(entityId)
        
        if entity.get_position().to_square().x > self.__weight: # не работает
            return entity.set_position(
                PixelVector(self.__weight, entity.get_position().y))
        elif entity.get_position().to_square().x < 0:
            return entity.set_position(
                PixelVector(0, entity.get_position().y))
        elif entity.get_position().to_square().y > self.__height:
            return entity.set_position(
                PixelVector(entity.get_position().x, self.__height))
        elif entity.get_position().to_square().y < 0:
            return entity.set_position(
                PixelVector(entity.get_position().x, 0))
        else:
            return entity.move(radius)

    def object_exists(self, posSquare): # TODO: exception throwing

        return self.grid[posSquare.x][posSquare.y] is not 0

    def entity_exists(self, entityId):

        return entityId in self.entities

    def add_object(self, posSquare, objType): # TODO: exception throwing

        self.grid[posSquare.x][posSquare.y] = objType

    def add_entity(self, entity): # TODO: exception throwing

        entityId = self.__entityIds
        self.entities[entityId] = entity
        self.__entityIds += 1

        return entityId

    def remove_entity(self, entityId):

        del self.entities[entityId]

    def load(self, array):

        pass

    def update(self):

        pass

    def get_entities(self):

        return self.entities

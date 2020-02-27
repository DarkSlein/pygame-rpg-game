from logic.vectors import PixelVector
from logic.entities.Entity import Entity

class Character(Entity):

    def __init__(self, posPixel=PixelVector(0, 0), speed=1, direction="right",
                 maxHealth=30, health=30):
        
        Entity.__init__(self, posPixel, speed, direction)

        self.__health = health
        self.__maxHealth = maxHealth

    def shoot(self):

        pass

    def damage(self, value):

        if self.__health - value > self.__maxHealth:
            self.__health = self.__maxHealth
            return False

        self.__health = self.__maxHealth

        #if self.__health <= 0: dead
        return True

from logic.vectors import PixelVector
from logic.entities.Entity import Entity

class Player(Entity):

    def __init__(self, posPixel = PixelVector(0, 0), speed=1, direction="right"):

        self.__health = 30
        self.__maxHealth = 30
        self.__speed = speed # TODO: fix kostyl
        Entity.__init__(self, posPixel, speed, direction)

    def shoot(self):

        pass

    def damage(self, value):

        if self.__health - value > self.__maxHealth:
            self.__health = self.__maxHealth
            return False

        self.__health = self.__maxHealth

        #if self.__health <= 0: dead
        return True

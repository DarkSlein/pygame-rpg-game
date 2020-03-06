from logic.vectors import PixelVector
from logic.entities.Entity import Entity

class Character(Entity):

    def __init__(self, map_, posPixel=PixelVector(0, 0), speed=1,
                 direction="right", name="tester", maxHealth=30, health=30):
        
        super().__init__(map_, posPixel, speed, direction)

        self.__name = name
        self.__health = health
        self.__maxHealth = maxHealth

    def shoot(self):

        pass

    def damage(self, value):

        if self.__health - value > self.__maxHealth:
            self.__health = self.__maxHealth
            return False

        self.__health -= value

        #if self.__health <= 0: dead
        return True

    def get_name(self):

        return self.__name

    def cast(self):

        pass

    def update(self):

        super().update()

        if self.__health < 0: # TODO: health < -constitution
            self.set_action("dead")

from logic.entities.Entity import Entity

class Player(Entity):

    def __init__(self):

        self.__health = 30
        self.__maxHealth = 30

    def shoot(self):

        pass

    def damage(self, value):

        if self.__health - value > self.__maxHealth:
            self.__health = self.__maxHealth
            return false

        self.__health = self.__maxHealth

        #if self.__health <= 0: dead
        return true

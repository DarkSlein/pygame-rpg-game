import random

from logic.entities.Character import Character

ACTION_TIMEOUT = 200

class AI:

    def __init__(self, character, map_):

        self.__character = character
        self.__map = map_
        self.__actionIterator = 0

    def control(self):

        self.__character.set_action("walking")
        
        if self.__character.get_got_obstacle() or \
        self.__actionIterator > ACTION_TIMEOUT:
            directions = ["left", "right", "up", "down"]
            self.__character.set_direction(directions[random.randrange(4)])
            self.__actionIterator = 0

        self.__actionIterator += 1

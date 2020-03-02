import random

from logic.entities.Character import Character

class AI:

    def __init__(self, character):

        self.__character = character

    def control(self):

        self.__character.set_action("walking")
        
        if self.__character.get_got_obstacle():
            directions = ["left", "right", "up", "down"]
            self.__character.set_direction(directions[random.randrange(4)])

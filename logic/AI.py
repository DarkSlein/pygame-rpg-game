import random

from logic.entities.Character import Character

class AI:

    def __init__(self, logic):

        self.__logic = logic

    def control(self, character):

        character.set_action("walking")
        
        if character.get_got_obstacle():
            directions = ["left", "right", "up", "down"]
            character.set_direction(directions[random.randrange(4)])

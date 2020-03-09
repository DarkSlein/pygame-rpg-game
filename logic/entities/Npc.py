from logic.vectors import PixelVector
from logic.entities.Character import Character
from logic.AI import AI

class Npc(Character):

    def __init__(self, map_, posPixel=PixelVector(0, 0), speed=1,
                 direction="right", size=PixelVector(40, 64),
                 name="npc_test", maxHealth=30, health=30):
        
        Character.__init__(self, map_, posPixel, speed,
                           direction, size,
                           name, maxHealth, health)

        self.__ai = AI(self, map_)

    def update(self):

        Character.update(self)

        self.__ai.control()

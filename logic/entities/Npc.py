from logic.vectors import PixelVector
from logic.entities.Character import Character

class Npc(Character):

    def __init__(self, posPixel=PixelVector(0, 0), speed=1, direction="right",
                 name="npc_test", maxHealth=30, health=30):
        
        Character.__init__(self, posPixel, speed, direction,
                           name, maxHealth, health)

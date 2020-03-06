from logic.vectors import PixelVector
from logic.entities.Character import Character
from logic.entities.Fireball import Fireball
from logic.functions import *

class Player(Character):

    def __init__(self, map_, posPixel=PixelVector(0, 0), speed=1,
                 direction="right", name="tester", maxHealth=30, health=30):
        
        super().__init__(map_, posPixel, speed,
                         direction, name, maxHealth, health)

    def cast(self):

        projPos = shift_position(self.get_position().copy(),
                                 self.get_direction(),
                                 30) # TODO: proj size
        self.get_map().add_entity(Fireball(self.get_map(), self,
                                       posPixel=projPos,
                                       direction=self.get_direction()))


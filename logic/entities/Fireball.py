from logic.entities.Projectile import Projectile
from logic.vectors import PixelVector

class Fireball(Projectile):

    def __init__(self, map_, owner, posPixel = PixelVector(0, 0),
                 speed=1, direction="right",
                 damage=5, damageType="physical"):

        Projectile.__init__(self, map_, owner, posPixel, speed, direction)

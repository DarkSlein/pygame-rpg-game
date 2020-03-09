from logic.entities.Projectile import Projectile
from logic.vectors import PixelVector

class Fireball(Projectile):

    def __init__(self, map_, owner, posPixel = PixelVector(0, 0),
                 speed=1, direction="right", size=PixelVector(20, 20),
                 damage=5, damageType="fire"):

        super().__init__(map_, owner, posPixel, speed, direction, size,
                         damage, damageType)

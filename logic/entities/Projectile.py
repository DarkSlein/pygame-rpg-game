from logic.Entity import Entity
from logic.vectors import PixelVector

class Projectile(Entity):

    def __init__(self, map_, posPixel = PixelVector(0, 0),
                 speed=1, direction="right"):

        Entity.__init__(map_, posPixel, speed, direction)

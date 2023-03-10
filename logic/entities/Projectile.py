from logic.entities.Entity import Entity
from logic.entities.Character import Character
from logic.vectors import PixelVector

class Projectile(Entity):

    def __init__(self, map_, owner, posPixel = PixelVector(0, 0),
                 speed=1, direction="right", size=PixelVector(40, 64),
                 damage=5, damageType="physical"):

        super().__init__(map_, posPixel, speed, direction, size)
        self.__owner = owner
        self.__damage = damage
        self.__damageType = damageType

        self.set_action("flying")

    def on_obstacle(self, entity=None):

        if entity and issubclass(type(entity), Character) and \
           entity != self.__owner:
            entity.damage(self.__damage)

        self.set_action("destroyed")

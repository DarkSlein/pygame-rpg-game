from logic.vectors import PixelVector
from logic.functions import *

class Entity:

    def __init__(self, map_, posPixel=PixelVector(0, 0),
                 speed=1, direction="right", size=PixelVector(40, 64)):

        self.__map = map_
        self.__posPixel = posPixel
        self.__speed = speed
        self.__status = "standing"
        self.__direction = direction
        self.__gotObstacle = False
        self.__size = size

    def update(self):

        pass

    def get_position(self):

        return self.__posPixel

    def set_position(self, posPixel):

        self.__posPixel = posPixel

    def get_direction(self):

        return self.__direction

    def set_direction(self, direction):

        self.__direction = direction

    def get_size(self):

        return self.__size

    def set_size(self, size):

        self.__size = size

    def move(self, radius=1): # TODO: dir as radians

        if self.__direction == "left":
            self.__posPixel.x -= int(radius*self.__speed)
        elif self.__direction == "right":
            self.__posPixel.x += int(radius*self.__speed)
        elif self.__direction == "up":
            self.__posPixel.y -= int(radius*self.__speed)
        elif self.__direction == "down":
            self.__posPixel.y += int(radius*self.__speed)

    def set_action(self, status):

        if self.__status == "dead":
            return

        self.__status = status

    def resurrect(self):

        if self.__status == "dead":
            self.__status = "standing"

    def get_action(self):

        return self.__status

    def get_speed(self):

        return self.__speed

    def set_got_obstacle(self, value):

        self.__gotObstacle = value

    def get_got_obstacle(self):

        return self.__gotObstacle

    def on_obstacle(self, entity=None):

        pass

    def get_map(self):

        return self.__map

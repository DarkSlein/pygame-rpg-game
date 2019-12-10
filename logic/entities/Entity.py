from logic.PixelVector import PixelVector

class Entity:

    def __init__(self, posPixel = PixelVector(0, 0), speed=1, direction="right"):

        self.__posPixel = posPixel
        self.__speed = speed
        self.__status = "standing"
        self.__direction = direction

    def get_position(self):

        return self.__posPixel

    def set_position(self, posPixel):

        self.__posPixel = posPixel

    def move(self, radius=1): # TODO: dir as radians

        if self.__direction == "left":
            self.__posPixel.x -= radius*self.__speed
        elif self.__direction == "right":
            self.__posPixel.x += radius*self.__speed
        elif self.__direction == "up":
            self.__posPixel.y -= radius*self.__speed
        elif self.__direction == "down":
            self.__posPixel.y += radius*self.__speed

    def set_action(self, status):

        self.__status = status

    def get_speed(self):

        return self.__speed

from logic.PixelVector import PixelVector

class SquareVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def toPixel(self):

        return PixelVector(self.x*32, self.y*32)

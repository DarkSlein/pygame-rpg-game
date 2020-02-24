class PixelVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def to_square(self):

        return SquareVector(int(self.x // 64), int(self.y // 64))

class SquareVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def to_pixel(self):

        return PixelVector(self.x*64, self.y*64)
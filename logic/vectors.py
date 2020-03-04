class PixelVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return "PixelVector(" + str(self.x) + ", " + str(self.y) + ")"

    def to_square(self):

        return SquareVector(int(self.x // 64), int(self.y // 64))

    def copy(self):

        return PixelVector(self.x, self.y)

class SquareVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return "SquareVector(" + str(self.x) + ", " + str(self.y) + ")"

    def to_pixel(self):

        return PixelVector(self.x*64, self.y*64)

    def copy(self):

        return SquareVector(self.x, self.y)

from logic.SquareVector import SquareVector

class PixelVector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def toSquare(self):

        SquareVector(self.x // 32, self.y // 32)

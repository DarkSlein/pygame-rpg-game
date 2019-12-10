import PixelVector
import SquareVector

def toPixelVector(posSquare):

    return PixelVector(posSquare.x*32 + 16, posSquare.y*32 + 16)

def toSquareVector(posPixel):

    return SquareVector(int((posPixel.x - 16)/32), int((posPixel.y - 16)/32))    

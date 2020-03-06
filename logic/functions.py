from logic.vectors import PixelVector, SquareVector

def shift_position(pos, direction, radius):

    resultPos = pos

    if direction == "left":
        resultPos.x -= int(radius)
    elif direction== "right":
        resultPos.x += int(radius)
    elif direction == "up":
        resultPos.y -= int(radius)
    elif direction == "down":
        resultPos.y += int(radius)

    return resultPos

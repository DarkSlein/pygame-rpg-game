class GameObject:

    def __init__(self, i=0, j=0, walkable=True, shootable=True):

        self.i = i
        self.j = j
        self.walkable = walkable
        self.shootable = shootable

class Camera:

    def __init__(self,x,y,scene):

        self.x = x
        self.y = y
        self.width = 480 # self.scene.map.size.x*16
        self.height = 640 # self.scene.map.size.y*16
        self.scene = scene

    def update(self,time):

        playerPos = self.scene.get_player_position()

        if playerPos.x - self.x < 1:
            self.x = playerPos.x - 500
        elif playerPos.x - self.x > 1:
            self.x = playerPos.x - 500

        if self.x < 0:
            self.x = 0
        elif self.x > self.width:
            self.x = self.width

        if playerPos.y - self.y < 1:
            self.y = playerPos.y - 280
        elif playerPos.y - self.y > 1:
            self.y = playerPos.y - 280

        if self.y < 0:
            self.y = 0
        elif self.y > self.height:
            self.y = self.height

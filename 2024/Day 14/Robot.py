class Robot():
    def __init__(self, startX, startY, velocityX, velocityY):
        self.x = int(startX)
        self.y = int(startY)
        self.velocityX = int(velocityX)
        self.velocityY = int(velocityY)

    def calculateNewPosition(self):
        self.x = (self.x + 100 * self.velocityX) % 101
        self.y = (self.y + 100 * self.velocityY) % 103

    def calculateNextPosition(self):
        self.x = (self.x + self.velocityX) % 101
        self.y = (self.y + self.velocityY) % 103

    def getPos(self):
        return [self.x, self.y]

    def getQuadrant(self):
        if(self.x < 101 // 2):
            if(self.y < 103 // 2):
                return 0
            elif(self.y > 103 // 2):
                return 2
        elif(self.x > 101 // 2):
            if(self.y < 103 // 2):
                return 1
            elif(self.y > 103 // 2):
                return 3
        return -1

    def __str__(self):
        return "Robot is at [" + str(self.x) + "|" + str(self.y) + "], with a velocity of [" + str(self.velocityX) + "|" + str(self.velocityY) + "]"
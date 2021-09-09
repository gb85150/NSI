import math

class Angles()

    def __init__(self):
        self.__angle = 0
        if __angle >= 360:
            __angle %= 360

    def getAngle(self):
        return "L'angle fait {} degrés".format(self.__angle)

    def setAngle(self, angle):
        self.__angle = angle
        return "Success"

    def getCos(self):
        return math.cos(self.__angle * math.pi / 180)

    def getSin(self):
        return math.sin(self.__angle * math.pi / 180)

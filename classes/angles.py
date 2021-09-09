import math

class Angles()

    def __init__(self):
        self.__angle = 0
        if __angle >= 360:
            __angle %= 360

    def getangle(self):
        return "L'angle fait {} degrés".format(self.__angle)

    def setangle(self, angle):
        self.__angle = angle
        return "Success"

    def getcos(self):
        return math.cos(self.__angle * math.pi / 180)


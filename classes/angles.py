import math


class Angles:
    def __init__(self):
        self.__angle = 0
        if self.__angle >= 360:
            self.__angle %= 360

    def get_angle(self):
        return "L'angle fait {} degrés".format(self.__angle)

    def set_angle(self, angle):
        self.__angle = angle
        return "Success"

    def get_cos(self):
        return math.cos(self.__angle * math.pi / 180)

    def get_sin(self):
        return math.sin(self.__angle * math.pi / 180)

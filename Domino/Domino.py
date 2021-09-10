from Geoffrey import generate
import random
# Main project


class Dominos:
    """The dominos game is composed of tiles painted with two numbers from 0 to 6
    Two sides :
    - A from 0 to 6
    - B from 0 to 6
    """
    def __init__(self):
        self.__A = list
        self.__B = list
        self.__A += random.randint(0, 7)
        self.__B += random.randint(0, 7)
        pass


deck = generate(Dominos)

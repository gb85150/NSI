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
        self.__A = random.randint(0, 6)
        self.__B = random.randint(0, 6)

    def debug(self):
        print(self.__A)
        print(self.__B)


t = Dominos()
t.debug()
deck = generate(Dominos)
"""
        for i in range(28):
            for i in range(28):
                self.__B.append(random.randint(0, 6))
                self.__A.append(random.randint(0, 6))
"""

from Geoffrey import generate
import random
# Main project
class Dominos:
    """The dominos game is composed of tiles painted with two numbers from 0 to 6
    """
    def __init__(self):
        self.A = random(0, 7)
        pass

deck = generate()
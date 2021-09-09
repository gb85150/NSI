class Satellite(name="KW667BE", weight=1500, speed=1500000):
    """docstring for Satellite."""
    __nom = str
    __masse = 100
    __vitesse = 0
    def __init__(self, name, weight, speed):
        self.__nom = name
        self.__masse = weight
        self.__vitesse = speed
        pass

    def impulsion(self, force, durée):
        deltaV = force * durée / self.__masse
        return deltaV

    def printspeed(self):
        return print("Le Satellite immatriculé {} se déplace actuellement à une vitesse de {} m/s".format(self.__name, self.__weight))

    def kinetic_energy(self):
        ke = (self.__masse * self.__vitesse) ** 2 / 2
        return print("L'énergie cinétique accumulée par le satellte est de {} J".format(ke))

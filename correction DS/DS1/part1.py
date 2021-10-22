class Rectangle:
    def __init__(self, long, larg):
        self.__largeur = larg
        self.__longueur = long

    def perimeter(self):
        return 2 * self.__largeur + 2 * self.__longueur

    def aire(self):
        return self.__largeur * self.__longueur

    def grossir(self, delta):
        self.__largeur = self.__largeur + delta
        self.__longueur = self.__longueur + delta

    def __lt__(self, rect):
        return self.aire() < rect.aire()


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.aire())
    print(rect.perimeter())
    rect.grossir(2)
    print(rect.aire())
    print(rect.perimeter())

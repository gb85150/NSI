import random as r


class Tas_de_pieces():
    """
    Un tas de pièces
    """
    def __init__(self):
        """init"""
        self.__tas = []

    def ajouter(self, pieces) -> None:
        """
        Ajoute des pièces
        """
        self.__tas.append(pieces)

    def est_vide(self) -> bool:
        """
        Teste si le tas est vide
        """
        if len(self.__tas) == 0:
            return True
        else:
            return False

    def piocher(self):
        """
        Pioche une pièce au hasard
        """
        random = r.randint(0, len(self.__tas))
        rng = self.__tas[random]
        self.__tas.remove(random)
        return rng

    def diviser(self):
        pass

    def peser(self):
        """
        Retourne la masse du tas
        """
        for i in range(len(self.__tas)):
            total = self.__tas[i]
            return total

    def taille(self):
        """
        Retourne la taille du tas
        """
        for i in range(len(self.__tas)):
            total = self.__tas[i]
            return total


class Piece:
    """
    Une pièce
    """
    def __init__(self, valeur: int, masse: int) -> None:
        """
        :param valeur: La valeur monétaire de la pièce
        :param masse:  La masse de la pièce
        """
        self.__valeur = valeur
        self.__masse = masse

    def get_valeur(self):
        return self.__valeur

    def get_masse(self):
        return self.__masse


def trouver_fausse_piece(tas):
    if tas.taille() == 1:
        return tas.piocher()

    else:
        tas_a, tas_b = tas.diviser()
    if tas_a.peser() % 10 == 9:
        return trouver_fausse_piece(tas_a)
    else:
        return trouver_fausse_piece(tas_b)


print(trouver_fausse_piece(Tas_de_pieces()))

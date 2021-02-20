if __name__ == '__main__':
    def tri(T: list, cle: str) -> list:
        """
        Fonction qui renvoie un tableau trié selon une clé définie en paramètre
        le tableau est vide en cas d'erreur de clé
        :param T: le tableau de départ
        :param cle: la clé de tri
        :return: une liste
        """

        tab = []
        if cle == "debut":
            tab = sorted(T, key=lambda x: x[1])
        elif cle == "fin":
            tab = sorted(T, key=lambda x: x[2])
        elif cle == "duree":
            for i in range(len(locations)):
                tmp_1 = locations[i][1]
                tmp_2 = locations[i][2]
                int(tmp_1)
                int(tmp_2)
                tmp = tmp_2 - tmp_1
                locations[i].append(tmp)
            tab = sorted(T, key=lambda x: x[3])
        else:
            tab = []
        return tab

    def Camion_occupe(jour: int, freetruck: bool) -> bool:
        """
        Détermine si le camion est dispo pour la location.
        :param jour: le jour actuel
        :param freetruck: la dispo initiale du camion
        :return: La disponibilité du camion
        """
        pass
        if freetruck is True:
            findloc(jour, locations)
        else:
            jour += 1
            freetruck = True
        return freetruck

    def findloc(jour: int, locations: list) -> bool:
        """
        Trouve les locations disponibles pour une rentabilité maximum
        :param jour: le jour actuel
        :param locations: la liste des demades de locations
        """
        i = -1
        ended = False
        while ended is False:
            i += 1
            if locations[i][1] >= jour:
                planning.append(locations[i][1])
                ended = True
                freetruck = False
            else:
                break
        return freetruck
        pass

    jour = 0
    freetruck = True
    locations = [[1, 1, 8], [2, 2, 5], [3, 4, 7], [4, 1, 3], [5, 5, 9],
                 [6, 8, 11], [7, 9, 10], [8, 13, 16], [9, 11, 14]]
    planning = []
    longueurplanning = 16
    for i in range(longueurplanning):
        Camion_occupe(jour, freetruck)
    # DEBUG: print all functions
    print(tri(locations, "debut"))
    print(tri(locations, "fin"))
    print(tri(locations, "duree"))
    print(planning)

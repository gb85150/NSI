class Graphe_m:
    """
    Un graphe représenté par une matrice d'adjacence,
    où les sommets sont les entiers 0, 1, 2, n-1
    """
    def __init__(self, n):
        self.__n = n
        self.__adj = [[False] * n for i in range(n)]

    def get_nb_sommets(self):
        return self.__n

    def get_adj(self):
        return self.__adj

    def ajouter_arc(self, s1, s2):
        self.__adj[s1][s2] = True

    def arc(self, s1, s2):
        return self.__adj[s1][s2]

    def voisins(self, s):
        v = []
        for i in range(self.__n):
            if self.__adj[s][i]:
                v.append(i)
        return v

    def afficher(self):
        for s in range(self.__n):
            print(s, "-->", end="")
            for v in range(self.__n):
                if self.__adj[s][v]:
                    print("", v, end="")
            print()

    def supprimer_arc(self, s1, s2):
        self.__adj[s1][s2] = False


class Graphe_d:
    """
    Un graphe représenté par un dictionnaire d'adjacence,
    plus exactement par un dictionnaire d'ensembles
    """
    def __init__(self):
        self.__adj = {}

    def get_adj(self):
        return self.__adj

    def get_nb_sommets(self):
        return len(self.__adj)

    def ajouter_sommet(self, s):
        if s not in self.__adj:
            self.__adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.__adj[s1].add(s2)

    def arc(self, s1, s2):
        if s1 in self.__adj:
            return s2 in self.__adj[s1]
        else:
            return "le sommet n'existe pas"

    def sommets(self):
        return list(self.__adj)

    def voisins(self, s):
        return self.__adj[s]

    def afficher(self):
        for s in self.__adj:
            if len(self.__adj[s]) == 0:
                print(s, "--> {}")
            else:
                print(s, "-->", self.__adj[s])

    def supprimer_arc(self, s1, s2):
        self.__adj[s1].remove(s2)

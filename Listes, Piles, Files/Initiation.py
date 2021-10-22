from dataclasses import dataclass


def inserer(lst, element, i):
    """Permet d' insérer un élément dans une liste à l' indice i"""
    if lst[0] == len(lst):
        raise IndexError("La liste est pleine")

    if i - 1 > lst[0]:
        raise IndexError("L' indice choisi est trop grand")

    for k in range(lst[0] + 1, i, -1):
        lst[k] = lst[k - 1]

    lst[i] = element
    lst[0] = lst[0] + 1


def longueur(lst):
    """Renvoie la longueur d' une liste"""
    return lst[0]


def supprimer(lst, i):
    """Permet la suppression d' un élément placé à l' indice i d' une liste"""
    if lst[0] == len(lst):
        raise IndexError("La liste est pleine")

    if i - 1 > lst[0]:
        raise IndexError("L' indice choisi est trop grand")
    pass


@dataclass
class Cellule:
    valeur: int
    suivante: object


class Liste:
    """une liste chaînée"""

    def __init__(self):
        self.debut = None

    def est_vide(self):
        return self.debut is None

    def tete(self):
        if self.est_vide():
            raise IndexError("Liste vide")
        return self.debut.valeur

    def queue(self):
        if self.est_vide():
            raise IndexError("Liste vide")
        l = Liste()
        l.debut = self.debut.suivante
        return l

    def cons(self, v):
        self.debut = Cellule(v, self.debut)

    def __len__(self):
        n = 0
        c = self.debut
        while c is not None:
            n += 1
            c = c.suivante
            return n

    def __str__(self):
        chaine = "valeurs de la liste = "
        c = self.debut
        while c is not None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante


cell = Cellule(suivante=5, valeur=4)
print(cell)

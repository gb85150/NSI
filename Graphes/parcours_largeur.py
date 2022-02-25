from classe_graphe import Graphe_d

class Cellule:
    """Une cellule de liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def ajouter(self, v):
        """- prend en paramètre une file et une valeur v
        - ajoute la valeur v à l'arrière de la file
        """
        c = Cellule(v, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def retirer(self):
        """- prend en paramètre une file
        - défile l'élément situé à l'avant de la file
        - renvoie la valeur défilée ou None si la file est vide
        """
        if self.est_vide():
            raise IndexError("La file est vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v

    def valeurs(self):
        chaine = "valeurs de la file = "
        c = self.tete
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def __str__(self):
        chaine = "valeurs de la file = "
        c = self.tete
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def __len__(self):
        l = 0
        c = self.tete
        while c != None:
            l = l + 1
            c = c.suivante
        return l

class Cellule:
    """Une cellule de liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

class Pile:
    """Structure de pile"""

    def __init__(self):
        self.contenu = None

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)

    def sommet(self):
        if self.est_vide():
            raise IndexError("Pile vide")
        v = self.contenu.valeur
        return v

    def depiler(self):
        if self.est_vide():
            raise IndexError("pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v

    def __str__(self):
        chaine = "valeurs de la pile = "
        c = self.contenu
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def valeurs(self):
        chaine = "valeurs de la pile = "
        c = self.contenu
        while c != None:
            chaine = chaine + str(c.valeur) + " "
            c = c.suivante
        return chaine

    def __len__(self):
        l = 0
        c = self.contenu
        while c != None:
            l = l + 1
            c = c.suivante
        return l

def parcours_largeur(G, s):
    f= File()
    f.ajouter(s)
    decouverts = []
    while f:
        s = f.retirer()
        decouverts.append(s)
        for v in G.voisins(s):
            if v not in decouverts and v not in f.valeurs():
                f.ajouter(v)
    return decouverts


def parcours_profondeur(s):
    p = Pile()
    p.empiler(s)
    visites = []
    while p:
        s = p.depiler()
        visites.append(s)
        for v in G.voisins(s):
            if v not in visites and v not in p.valeurs():
                p.empiler(v)
    return visites


if __name__ == "__main__":
    G = Graphe_d()
    G.ajouter_arc("A", "B")
    G.ajouter_arc("A", "C")
    G.ajouter_arc("A", "D")
    G.ajouter_arc("B", "E")
    G.ajouter_arc("C", "E")
    G.ajouter_arc("D", "E")
    G.ajouter_arc("E", "F")
    G.ajouter_arc("E", "G")
    G.ajouter_arc("F", "H")
    G.ajouter_arc("G", "H")
    G.ajouter_arc("H", "I")
    G.ajouter_arc("I", "J")
    G.ajouter_arc("J", "K")
    G.ajouter_arc("K", "L")
    G.ajouter_arc("K", "M")
    G.ajouter_arc("L", "M")
    G.ajouter_arc("M", "N")
    G.ajouter_arc("N", "O")
    G.ajouter_arc("O", "P")
    G.ajouter_arc("P", "Q")
    print(parcours_profondeur(G, "A"))
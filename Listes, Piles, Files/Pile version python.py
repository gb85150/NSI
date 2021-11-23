class Pile:
    def __init__(self):
        self.liste = []

    def empiler(self, element):
        self.liste.append(element)

    def depiler(self):
        return self.liste.pop()

    def est_vide(self):
        return len(self.liste) == 0

    def taille(self):
        return len(self.liste)

    def sommet(self):
        return self.liste[-1]

    def afficher(self):
        print(self.liste)

    def __str__(self) -> str:
        chaine = "valeurs de la pile :"
        for element in self.liste: # parcours de la liste
            chaine += " " + str(element)
        return chaine

class Cellule: # cellule de la file
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

    def afficher(self):
        print(self.valeur)


class File:
    def __init__(self):
        self.premier = None
        self.dernier = 0
        self.dernier.suivant = None

    def est_vide(self):
        return self.premier == None

    def enfiler(self, element):
        if self.est_vide():
            self.premier = element
            self.dernier = element
        else:
            self.dernier.suivant = element
            self.dernier = element

    def defiler(self):
        if self.est_vide():
            print("La file est vide")
        else:
            valeur = self.premier.valeur
            self.premier = self.premier.suivant
            return valeur

    def afficher(self):
        if self.est_vide():
            print("La file est vide")
        else:
            cellule = self.premier
            while cellule != None:
                cellule.afficher()
                cellule = cellule.suivant


def polonaise_inverse(chaine):
    pile = Pile()
    for element in chaine.split(" "):
        if element.isdigit():
            pile.empiler(element)
        else:
            operande2 = pile.depiler()
            operande1 = pile.depiler()
            pile.empiler(str(eval(operande1 + element + operande2)))
    return pile.depiler()


def survivant(file) -> int:
    """
    Précondition : file est une file de nombres
    Postcondition : retourne le nombre de survivants
    Par exemple : survivant(File([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) retourne 5
    Dans cette exemple, les nombres 1, 2, 3, 4, 5 sont les survivants
    """
    if file.est_vide():
        return 0
    else:
        return file.defiler() + survivant(file)


if __name__ == "__main__":
    print(polonaise_inverse("1 2 3 + 3 7 * + *"))
    fle = File()
    for i in range(10):
        fle.enfiler(i)
    survivant(fle)
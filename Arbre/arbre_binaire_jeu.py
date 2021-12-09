import turtle as t

class Noeud:
    """Un noeud d'arbre binaire"""
    def __init__(self, valeur=None, gauche=None, droite=None):
        self.__valeur = valeur
        self.__gauche = gauche
        self.__droite = droite
    
    def est_vide(self) -> bool:
        return self.__valeur is None
    
    def get_gauche(self):
        return self.__gauche
    
    def get_droite(self):
        return self.__droite
    
    def get_valeur(self):
        return self.__valeur
    
    def set_gauche(self, gauche):
        self.__gauche = gauche
    
    def set_droite(self, droite):
        self.__droite = droite
    
    def set_valeur(self, valeur):
        self.__valeur = valeur
    
    def pprint(self, indent=0):
        if self.get_droite():
            self.get_droite().pprint(indent + 1)
        print("{}{}".format(" " * 4 * indent, self.get_valeur()))
        if self.get_gauche():
            self.get_gauche().pprint(indent + 1)
        

def taille(arbre):
    """Renvoie la taille de l'arbre"""
    if arbre is None:
        return 0
    else:    
        return 1 + taille(arbre.get_gauche()) + taille(arbre.get_droite())


def hauteur(arbre):
    """Renvoie la hauteur de l'arbre"""
    if arbre is None:
        return 0
    return 1 + max(hauteur(arbre.get_gauche()), hauteur(arbre.get_droite()))


def feuilles(arbre: Noeud) -> str:
    """Renvoie le nombre de feuilles de l'arbre"""
    if arbre is None:
        return ""
    else:
        if arbre.get_gauche() is None and arbre.get_droite() is None:
            return 1
        else:
            return str(feuilles(arbre.get_gauche())) + " " + str(feuilles(arbre.get_droite()))


def infixe(arbre: Noeud) -> str:
    """Renvoie la représentation infixe de l'arbre"""
    if arbre is not None:
        infixe(arbre.get_gauche())
        print(arbre.get_valeur(), end=" ")
        infixe(arbre.get_droite())


def prefixe(arbre: Noeud) -> str:
    """Renvoie la représentation prefixe de l'arbre"""
    if arbre is not None:
        print(arbre.get_valeur(), end=" ")
        prefixe(arbre.get_gauche())
        prefixe(arbre.get_droite())


def suffixe(arbre: Noeud) -> str:
    """Renvoie la représentation suffixe de l'arbre"""
    if arbre is not None:
        suffixe(arbre.get_gauche())
        suffixe(arbre.get_droite())
        print(arbre.get_valeur(), end=" ")


def parcours_largeur(arbre):
    queue = []
    queue.append(arbre)

    while len(queue) > 0:
        # On récupère le premier élément de la file
        print(queue[0].get_valeur(), end=" ")
        # On le supprime de la file
        node = queue.pop(0)

        #ajouter l'enfant gauche de l'élément retiré à la file
        if node.get_gauche() is not None:
            queue.append(node.get_gauche())
        #ajouter l'enfant droit de l'élément retiré à la file
        if node.get_droite() is not None:
            queue.append(node.get_droite())


def affichage(arbre: Noeud):
    """Affiche l'arbre"""
    if arbre is not None:
        def aller(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
        
        def cercle(x, y, r):
            aller(x, y - r)
            t.color("black", "lightgreen")
            t.begin_fill()
            t.circle(r)
            t.end_fill()
        
        def trace(n, arbre, x = 0, y = 200):
            """Trace récursivement l'arbre avec la tortue"""
            if arbre is None:
                t.pencolor("white") # si le sous-arbre est vide, on le trace en blanc
            else:
                t.pencolor("black")
            t.goto(x, y) # on se positionne sur la branche de l'arbre
            if n > 0 and arbre is not None:
                # position du prochain Noeud gauche
                gauche = (x - 2**(n - 1 + 7 - profondeur) * 3, y - 400 / (profondeur))
                # position du prochain Noeud droit
                droite = (x + 2**(n - 1 + 7 - profondeur) * 3, y - 400 / (profondeur))
                # appel récursif gauche
                trace(n - 1, arbre.get_gauche(), *gauche)
                aller(x, y)
                # appel récursif droit
                trace(n - 1, arbre.get_droite(), *droite)
                aller(x, y)
                cercle(x, y, 10 * (7 - profondeur)) # tracé du Noeud
                aller(x + 1, y - taille_police + 2)
                legende = arbre.get_valeur()
                t.write(f"{legende}", align="center", font=("Arial", taille_police, "normal"))
                aller(x - 1, y + taille_police - 2)

        if arbre is None:
            return None
        
        if arbre.get_valeur() is not None:
            #t.screensize(500, 500)
            t.speed("fastest") # vitesse maximale
            t.hideturtle() # on cache la tortue
            t.width(2) # épaisseur de 2 du crayon
            # calcul de la profondeur, nécessaire pour ajuster le tracé
            profondeur = hauteur(arbre) + 1
            taille_police = 27 - 3 * profondeur # calcul de la taille de la police
            aller(0, 200) # position de départ
            trace(profondeur, arbre) # appel de la fontion de tracé
            t.exitonclick() # on attend un click de la souris pour fermer la fenêtre


def ajoute(a, x):
    """ ajoute x à l'arbre, renvoie un nouvel arbre"""
    if x <= a.get_valeur():
        if a.get_gauche() is None:
            a.set_gauche(Noeud(x, None, None))
        else:
            ajoute(a.get_gauche(), x)
    if x > a.get_valeur():
        if a.get_droite() is None:
            a.set_droite(Noeud(x, None, None))
        else:
            ajoute(a.get_droite(), x)


if __name__ == "__main__":
    n1 = Noeud(1, Noeud(2), Noeud(3))
    n2 = Noeud(2)
    arbre = Noeud(99, n1, n2)
    arbre.pprint()
    void = Noeud()
    for i in range(3):
        ajoute(arbre, i)
    print(void.est_vide())
    print("nb de feuilles: {}".format(feuilles(arbre)))
    print("taille: {}".format(taille(arbre)))
    print("hauteur: {}".format(hauteur(arbre)))
    prefixe(arbre)
    suffixe(arbre)
    infixe(arbre)
    affichage(arbre)
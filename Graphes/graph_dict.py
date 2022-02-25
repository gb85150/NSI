class D_Graph:
    """
    Une implémentation du graphe par dictionnaire, ses fonctions sont :
    - Afficahge des voisins
    - Ajout des sommets
    - Ajout des arcs
    - Vérification de la présence d'un arc
    - Vérification de la présence d'un sommet
    - Suppression d'un arc
    - Suppression d'un sommet
    - Retourne la liste des sommets
    - Retourne la liste des arcs
    Les dictionnaires sont composés d'ensembles
    """
    def __init__(self) -> None:
        """
        Initialise le graphe
        """
        self.Graph = {}
    
    def ajouter_sommet(self, node: int) -> None:
        """
        Ajoute un sommet au graphe
        """
        if node not in self.Graph:
            self.Graph[node] = set()
    
    def ajouter_arc(self, node1: int, node2: int, sens=0) -> None:
        """
        Ajoute un arc entre deux sommets
        """
        self.ajouter_sommet(node1)
        self.ajouter_sommet(node2)
        if sens == 0:
            self.Graph[node1].add(node2)
            self.Graph[node2].add(node1)
        elif sens == 1:
            self.Graph[node1].add(node2)
        elif sens == 2:
            self.Graph[node2].add(node1)
    
    def voisin(self, node: int) -> list:
        """
        Retourne la liste des voisins d'un sommet
        """
        return list(self.Graph[node])
    
    def arc(self, node1: int, node2: int, sens=0) -> bool:
        """
        Retourne True si l'arc existe
        """
        if node2 in self.Graph[node1] and node1 in self.Graph[node2] and sens == 0:
            return True
        elif sens == 1 and node2 in self.Graph[node1]:
            return True
        elif sens == 2 and node1 in self.Graph[node2]:
            return True
        else:
            return False
    
    def sommet(self, node: int) -> bool:
        """
        Retourne True si le sommet existe
        """
        return node in self.Graph
    
    def supprimer_arc(self, node1: int, node2: int) -> None:
        """
        Supprime un arc
        """
        self.Graph[node1].remove(node2)
        self.Graph[node2].remove(node1)

    def supprimer_sommet(self, node: int) -> None:
        """
        Supprime un sommet
        """
        for voisin in self.Graph[node]:
            self.Graph[voisin].remove(node)
        del self.Graph[node]
    
    def liste_sommets(self) -> list:
        """
        Retourne la liste des sommets
        """
        return list(self.Graph.keys())
    
    def liste_arcs(self) -> list:
        """
        Retourne la liste des arcs
        """
        return list(self.Graph.values())

    def __str__(self) -> str:
        """
        Affiche les noeuds et leurs voisins sous la forme :
        0 -> 1 3
        """
        res = ""
        for node in self.Graph:
            res += str(node) + " -> " + " ".join(str(x) for x in self.Graph[node]) + "\n"
        return res


if __name__ == '__main__':
    G1 = D_Graph()
    G1.ajouter_sommet(0)
    G1.ajouter_sommet(1)
    G1.ajouter_sommet(2)
    G1.ajouter_sommet(3)
    G1.ajouter_arc(0, 1)
    G1.ajouter_arc(0, 2)
    G1.ajouter_arc(1, 2)
    G1.ajouter_arc(2, 3)
    G1.ajouter_arc(3, 0)
    print(G1)
    print(G1.liste_sommets())
    print(G1.liste_arcs())
    G1.supprimer_arc(0, 1)
    G1.supprimer_arc(0, 2)
    G1.supprimer_arc(1, 2)
    G1.supprimer_arc(2, 3)
    G1.supprimer_arc(3, 0)
    print(G1)
    G1.supprimer_sommet(0)
    G1.supprimer_sommet(1)
    G1.supprimer_sommet(2)
    G1.supprimer_sommet(3)
    print(G1)
    print(G1.liste_sommets())
    print(G1.liste_arcs())
    print(G1.sommet(0))
    print(G1.sommet(1))
    print(G1.sommet(2))
    print(G1.sommet(3))
    print(G1.arc(0, 1))
    print(G1.arc(0, 2))
    print(G1.arc(1, 2))
    print(G1.arc(2, 3))
    print(G1.arc(3, 0))
    print(G1.voisin(0))

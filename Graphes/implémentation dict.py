class Graphe_d:
    """
    Graphe à base de dictionnaires de dépendance
    """
    def __init__(self) -> None:
        self.Graph = {}
    
    def add_edge(self, node1: int, node2: int) -> None:
        """
        Ajoute un arc entre les noeuds
        """
        if node1 in self.Graph:
            self.Graph[node1].append(node2)
        else:
            self.Graph[node1] = [node2]

    def add_node(self, node: int, rel: list) -> None:
        """
        Ajoute un noeud au graphe
        """
        self.Graph[node] = rel
    
    def get_nearby(self, node: int) -> list:
        """
        Retourne la liste des noeuds voisins
        """
        return self.Graph[node]
    
    def is_linked(self, node1: int, node2: int) -> bool:
        """
        Retourne True si les noeuds sont reliés
        """
        return node2 in self.Graph[node1]
    
    def get_nodes(self) -> list:
        """
        Retourne la liste des noeuds
        """
        return list(self.Graph.keys())
    
    def __str__(self) -> str:
        """
        Affiche les noeuds et leurs voisins sous la forme :
        0 -> 1 3
        """
        res = ""
        for node in self.Graph:
            res += str(node) + " -> " + " ".join(str(x) for x in self.Graph[node]) + "\n"
        return res

if __name__ == "__main__":
    G = Graphe_d()
    G.add_node(0, [1, 2])
    G.add_node(1, [2, 3])
    G.add_node(2, [3])
    G.add_node(3, [])
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    print(G.is_linked(0, 1))
    print(G.is_linked(0, 2))
    print(G.is_linked(1, 2))
    print(G.is_linked(1, 3))
    print(G.is_linked(2, 3))
    print(G)

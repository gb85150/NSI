from math import sqrt
def distance(point1, point2):
    """
    Calcule et renvoie la distance entre deux points
    """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def plus_courte_distance(tab: list, depart: int):
    """
    Renvoie le point du tableau tab se trouvant à la plus
    courte distance du point depart.
    """
    point = tab[0]
    min_dist = distance(tab[0], depart)
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [2, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (7, 9)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)) == [5, 2], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (2, 5)) == [2, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 9)) == [5, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 7)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 5)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 2)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 0)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 9)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 5)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 2)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [7, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 9)) == [5, 9], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 5)) == [5, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)) == [5, 2], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (2, 5)) == [2, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (2, 2)) == [2, 2], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (2, 0)) == [2, 0], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 5)) == [0, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 2)) == [0, 2], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [0, 0], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 7)) == [9, 7], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 5)) == [9, 5], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 2)) == [9, 2], "erreur"
assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (9, 0)) == [9, 0], "erreur"
assert plus_courte_distance
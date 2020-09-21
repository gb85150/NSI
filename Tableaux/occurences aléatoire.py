# calcul random (ex 3)
# init
from random import randint
Tirage = []
Nbre_occurences = []


def count(valeur, tableau):
    countresult = 0
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            countresult += 1
    return countresult


# Tirage de 1000 entiers
Tirage.append(randint(1, 10)) for i in range(1000)
for i in range(1, 11):
    Nbre_occurences[i] = count(Tirage, i)
print(Nbre_occurences)
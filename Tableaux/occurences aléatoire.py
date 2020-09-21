# calcul random (ex 3)
# init
from random import randint
Tirage = []


def count(valeur, tableau):
    countresult = 0
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            countresult += 1
    return countresult


while restart? == y:
# Tirage de 1000 entiers
    Tirage=[randint(1, 10) for i in range(1000)]
    for i in range(1,11):
        print(count(i, Tirage))
    restart?=int(input("recommencer ? (y/n)"))

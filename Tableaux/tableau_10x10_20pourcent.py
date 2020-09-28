# tableau random
import random


def listgen():
    probabilité = (0, 0, 0, 0, 1)
    liste = [[random.choice(probabilité) for i in range(10)] for i in range(10)]
    return liste


def guessuser():
    x = int(input("sélectionnez la position de x (va de 1 à 10) "))
    y = int(input("sélectionnez la position de y (va de 1 à 10) "))
    guess = [x, y]
    return guess


def checktab(guess):
    x = guess[1]
    y = guess[0]
    if tab[x][y] == 1 :
        print("Tu as trouvé la position bravo !")
        score = 1
        return score
    else:
        print("Retente ta chance !")
        score = 0
        return score


def printtab():
    for i in range(10):
        print(tab[i])


def Main():
    # Calcul du nbre de 1
    nbde1 = 0
    score = 0
    for i in range(10):
        nbde1 = nbde1 + tab[i].count(1)
    print("il y a {} 1 dans ce tableau".format(nbde1))
    for i in (range(1, 4)):
        print("tentative n°{} : ".format(i))
        scoretentative = checktab(guessuser())
        score += scoretentative
    print("score = ", score)
    print("le tableau complet :")
    printtab()


# init
tab = listgen()
nbde1 = 0
Main()
if str(input("Recommencer ? (y/n): ")) == y :
    Main()
else:
    print("Merci d'avoir joué")
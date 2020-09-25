#tableau random
import random


def listgen():
    probabilité = (0,0,0,0,1)
    liste = [[random.choice(probabilité) for i in range(10)] for i in range(10)]
    return liste

def guessuser():
    x = int(input("sélectionnez la position de x (va de 1 à 10)"))
    y = int(input("sélectionnez la position de y (va de 1 à 10)"))
    guess = (x,y)
    return guess
test 


tab=listgen()
nbde1 = 0
for i in range(10):
    nbde1 = nbde1 + tab[i].count(1)
print(nbde1)
for i in (range(3)):
    print("tentative n°{} : ".format(i))
    guessnum{}.format(i) = guessuser()
# for i in range(10):
#     print(tab[i])
    
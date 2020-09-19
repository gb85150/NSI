from random import randint


def tabAleatiore(n, a, b):
    liste = [randint(a, b) for i in range(n)]
    return liste


number = int(input("le nombre d'entrées ? "))
mini = int(input("nombre min ? "))
maxi = int(input("nombre max ? "))
print(tabAleatiore(number, mini, maxi))

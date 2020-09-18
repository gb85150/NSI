from random import randint


def tabAleatiore(n, a, b):
    liste = [0] * n
    for i in range(n):
        liste[i] = randint(a, b)
    return liste


number = int(input("le nombre d'entrées ? "))
mini = int(input("nombre min ? "))
maxi = int(input("nombre max ? "))
print(tabAleatiore(number, mini, maxi))

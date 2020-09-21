# calcul random (ex 3)
# init
from random import randint
from custom_count import count
Tirage = []
while restart? == y:
    # Tirage de 1000 entiers
    Tirage = [randint(1, 10) for i in range(1000)]
    for i in range(1, 11):
        print(count(i, Tirage))
    restart? = int(input("recommencer ? (y/n)"))

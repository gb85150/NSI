from random import randint


def count(valeur, tableau):
    countresult = 0
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            countresult += 1
    return countresult


def occurences(v, t):
    return(count(v, t))


v = int(input("occurance à checker ? "))
liste = [randint(1, 10) for i in range(randint(1, 10))]
print(liste)
print(occurences(v, liste))
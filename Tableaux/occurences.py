from random import randint


def occurences(v, t):
    return(t.count(v))


v = int(input("occurance à checker ? "))
liste = [randint(1, 10) for i in range(randint(1, 10))]
print(liste)
print(occurences(v, liste))

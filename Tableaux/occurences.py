from random import randint
from custom_count import count


def occurences(v, t):
    return(count(v, t))


v = int(input("occurance à checker ? "))
liste = [randint(1, 10) for i in range(randint(1, 10))]
print(liste)
print(occurences(v, liste))

# devine nombre
from random import randint
nbremystere = randint(1, 1000)
trouve = False
while trouve == False:
    guess = int(input("choisis un entier entre 1 et 1000 : "))
    if guess == nbremystere:
        print("trouvé")
    else:
        if guess > nbremystere:
            print("le nombre à trouver est plus petit")
        else:
            if guess < nbremystere:
                print("le nombre à trouver est plus grand")

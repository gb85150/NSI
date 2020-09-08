# lancer de dés
from random import randint
nbretentatives = 0
resultat=0
while resultat != 6 :
    resultat = randint(1,6)
    nbretentatives = nbretentatives + 1
print(nbretentatives)
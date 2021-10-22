
# Functions de geoffrey
def generate(Dominos):
    jeu_dominos = []
    jeu_dominos.append(Dominos(0,0))
    for i in range(7):
      for k in range(i):
        jeu_dominos.append(Dominos(k, i))
    return jeu_dominos


def test_recurrence(dominos):
    double = []
    for i in range(28):
        if dominos.__A[i] == dominos.__B[i]:
            double += i
    return double
# Functions de geoffrey
def generate(dominos):
    jeu_dominos = list
    for i in range(28):
        jeu_dominos += dominos
    return jeu_dominos


def test_recurrence(dominos):
    double = list
    for i in range(28):
        if dominos.__A[i] == dominos.__B[i]:
            double += i
    return double

def start(nb_fire):
    state = []
    for i in range(nb_fire):
        state.append(False)
    return state


def children(state, jump):
    for i in range(0, 196, jump):
        if state[i]:
            state[i] = False
        else:
            state[i] = True
    return state


def main(nb_child, nb_fire):
    state = start(nb_fire)
    for i in range(nb_child):
        children(state, i + 1)
    return count(state)


def count(state: list):
    k1 = 0
    k2 = 0
    for i in range(len(state)):
        if state[i]:
            k1 += 1
        else:
            k2 += 1
    print("Feux allumés : {}\nFeux éteins : {}".format(k1, k2))


if __name__ == '__main__':
    main(nb_child=int(input("Nombre de gosses : ")), nb_fire=int(input("Nombre de guirlandes de Noel : ")))

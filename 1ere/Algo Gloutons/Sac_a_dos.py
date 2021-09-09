def remplissage(input: list, maxcapacity: int):
    bag = []
    maxcapacity = 40
    capacity = maxcapacity
    for i in input:
        if i['weight'] < capacity:
            bag.append(i)
            capacity = capacity - i['weight']
        for i in bag:
            print(i, flush=True)
    print(len(bag))


butin = [
    {'name': 'object1', 'weight': 15, 'value': 500},
    {'name': 'object2', 'weight': 24, 'value': 400},
    {'name': 'object3', 'weight': 9, 'value': 350},
    {'name': 'object4', 'weight': 25, 'value': 750},
    {'name': 'object5', 'weight': 5, 'value': 400},
    {'name': 'object6', 'weight': 12, 'value': 800},
    {'name': 'object7', 'weight': 2, 'value': 1400},
    {'name': 'object8', 'weight': 18, 'value': 550},
    ]
bestbutin = sorted(butin, key=(lambda x: x['value'] / x['weight']), reverse=True)
remplissage(bestbutin, 40)

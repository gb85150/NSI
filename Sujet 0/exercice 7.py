def fibonacci(int) -> int:
    """
    Calcule le dernier élément de la suite de fibonacci. Récursivité interdite.
    """
    n1 = 0
    n2 = 1
    for i in range(int):
        n1, n2 = n2, n1 + n2
    return n1


if __name__ == "__main__":
    print(fibonacci(10))
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(25) == 75025
    assert fibonacci(45) == 1134903170
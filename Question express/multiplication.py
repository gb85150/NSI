def multiplication(a, b):
    """
    Multiplie deux nombres a et b.
    Les seules opérations autorisées sont les additions et les soustractions.
    """
    if a == 0 or b == 0:
        return 0
    elif a > 0 and b > 0:
        for i in range(a):
            b += 1
        return b
    elif a < 0 and b < 0:
        for i in range(a):
            b -= 1
        return b
    elif a > 0 and b < 0:
        for i in range(a):
            b -= 1
        return b
    elif a < 0 and b > 0:
        a = 0 - a
        for i in range(a):
            b += 1
        return b

if __name__ == "__main__":
    print(multiplication(2, 3))
    print(multiplication(2, -3))
    print(multiplication(-2, 3))
    print(multiplication(-2, -3))
    print(multiplication(0, 3))
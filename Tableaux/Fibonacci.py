# Fibonacci
suite_fibonacci = [0, 1]
for i in range(2, 30):
    suite_fibonacci.append(suite_fibonacci[i-1]+suite_fibonacci[i-2])
if suite_fibonacci[29] == 514229:
    print(suite_fibonacci)
else:
  print(
        """
        FATAL ERROR
        erreur détectée veuillez controler votre code.

        La suite correcte est :
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
        55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
        6765, 10946, 17711, 28657, 46368, 75025, 121393,
        196418, 317811, 514229, 832040
        (Source : https://calculis.net/fibonacci)

        Voici toutes les variable connues au momemt de l'erreur
        """, suite_fibonacci)

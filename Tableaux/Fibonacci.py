# Fibonacci
suite_fibonacci = [0, 1]
for i in range(2, 31):
    suite_fibonacci.append(suite_fibonacci[i-1]+suite_fibonacci[i-2])
if suite_fibonacci[30] == 514229:
    print(suite_fibonacci)
else:
    print("erreur détectée")

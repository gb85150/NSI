#Fibonacci
suite_fibonacci = [0,1]
for i in range(2, 30):
    suite_fibonacci.append([i-1]+[i-2])
# try:
#     if suite_fibonacci[30] == 514229:
print(suite_fibonacci)
#     except SyntaxError
# print("erreur détectée")
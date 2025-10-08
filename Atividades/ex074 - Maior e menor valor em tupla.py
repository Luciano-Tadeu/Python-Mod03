from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os valores sorteados foram:", end=" ")
for c in numeros:
    print(f"{c}", end = " ")

print("\nO maior valor sorteado foi {}".format(max(numeros)))
print("O menor valor sorteado foi {}".format(min(numeros)))
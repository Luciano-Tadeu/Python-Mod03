from random import randint
from time import sleep

lista = randint(1, 10)
números = list()

for c in range(0, lista):
    números.append(randint(1, 10))

def organizador(lst):
    print("-="*25)
    print("Analisando os valores passados...")
    c = 0
    while c <= (len(lst) - 1):
        print(lst[c], end=' ', flush=True)
        c += 1
        sleep(0.5)
    print(f"Foram informados {len(lst)} valores ao todo.")
    print(f"O maior valor informado foi {max(lst)}")
    print("-="*25)

organizador(números)
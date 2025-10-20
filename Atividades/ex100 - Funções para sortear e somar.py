from random import randint
from time import sleep

def sortear():
    print("Sorteando 5 valores da lista: ", end='')
    lista = list()
    
    for c in range(0, 5):
        num = randint(1, 9)
        lista.append(num)

    for c in lista:
        print(c, end=" ", flush=True)
        sleep(0.5)
    print("PRONTO!")
    
    return lista

listaSomar = sortear()

def somarPares(lst):
    somaP = 0
    for c in lst:
        if c % 2 == 0:
            somaP += c
    print(f"Somando os valores pares de {lst}, temos {somaP}")

somarPares(listaSomar)
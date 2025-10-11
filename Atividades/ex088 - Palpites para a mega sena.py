from random import randint
from time import sleep

print("-"*30)
print("{:^30}".format("JOGA NA MEGA SENA"))
print("-"*30)

quant = int(input("Quantos jogos você quer que eu sorteie? "))
jogo = [[], [], [], [], [], []]
cont = 0

for c in range (0, quant):
    while cont != 6:
        num = randint(1, 60)
        if num not in jogo[c]:
            jogo[c].append(num)
            cont += 1
    cont = 0
    print(f"Jogo {c + 1}: {sorted(jogo[c])}")
    sleep(1)
print('-='*7, "{:^}".format("< BOA SORTE >"), '-='*7)
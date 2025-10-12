from random import randint
from time import sleep
from operator import itemgetter

dados = list()
jogador = dict()

for c in range(1, 5):
    jogador[f'jogada {c}'] = randint(1, 6)
    print(f"jogador {c} tirou {jogador[f'jogada {c}']} no dado.")
    sleep(0.5)

print("-="*20)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print("{:^30}".format("== RANKING JOGADORES =="))



for k, (v, c) in enumerate(ranking, start=1):
    print(f"{k}º jogador {v} tirou {c} no dado.")
    sleep(0.5)
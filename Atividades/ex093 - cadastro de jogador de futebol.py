dados = dict()

dados['nome'] = input("Nome do Jogador: ")
partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
sGols = 0
gols = list()

for c in range(0, partidas):
    gol = int(input(f'  Quantos gols na partida {c}? '))
    gols.append(gol)
    sGols += gol
    

dados['gols'] = gols
dados['total'] = sGols

print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f"O jogador {dados['nome']} jogou {partidas} partidas.")
for c, i in enumerate(gols):
    print(f" => Na partida {c}, fez {i} gols.")
print(f"Foi um total de {sGols} gols")
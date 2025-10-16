dados = dict()
totalDados = list()
while True:
    
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
    totalDados.append(dados.copy())
    
    while True:
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
        if sair in 'SN':
            break
        print("Digite apenas S ou N.")
    if sair == 'N':
        break


print("-="*30)
print("{:<5} {:<15} {:<15} {:<8}".format("cod", "nome", "gols", "total"))
print("-"*50)

for i, c in enumerate(totalDados):
    print("{:<5} {:<15} {:<15} {:<8}".format(i, c["nome"], str(c["gols"]), str(c["total"])))
        
print("-"*50)

while True:
    ind = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if ind == 999:
        break
    elif ind > (len(totalDados) - 1) or ind < 0:
        print(f"ERRO! Digite entre 0 e {len(totalDados) - 1}")
    else:
        nome = totalDados[ind]["nome"]
        print(f"-- LEVANTAMENTO DO JOGADOR {nome}:")
        gols = totalDados[ind]['gols']
        for n, c in enumerate(gols):
            print(f"    No jogo {n+1} fez {c} gols.")
    
dados = []
banco = []
count = 0

while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    banco.append(dados[:])
    if count == 0:
        pesoMaior = pesoMenor = dados[1]
    else:
        if dados[1] > pesoMaior:
            pesoMaior = dados[1]
        if dados[1] < pesoMenor:
            pesoMenor = dados[1]
    
    dados.clear()
    count += 1
    sair = ' '
    while sair not in 'SN':
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
    
    if sair == 'N':
        break

print("-="*30)
print(f"Ao todo você cadastrou {len(banco)} pessoas")
print(f"O maior peso foi de {pesoMaior}Kg. Peso de", end=' ')

for c in range(0, len(banco)):
    for i in range(0, 2):
        if banco[c][i] == pesoMaior:
            print(banco[c][i-1], end = ' ')
print()

print(f"O menor peso foi de {pesoMenor}Kg. Peso de", end='')

for c in range(0, len(banco)):
    for i in range(0, 2):
        if banco[c][i] == pesoMenor:
            print(banco[c][i-1], end = ' ')
print()
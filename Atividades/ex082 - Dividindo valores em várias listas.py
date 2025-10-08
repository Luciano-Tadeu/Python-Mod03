lista = []
listaPares = []
listaÍmpares = []
while True:
    lista.append(int(input("Digite um valor: ")))
    
    sair = ' '
    while sair not in 'SN':
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
    if sair == 'N':
        break
    
for c in lista:
    if c % 2 == 0:
        listaPares.append(c)
    else:
        listaÍmpares.append(c)
        
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listaPares}")
print(f"A lista de ímpares é {listaÍmpares}")


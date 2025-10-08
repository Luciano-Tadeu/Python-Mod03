lista = []

while True:
    
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado! Não será adicionado...")
    
    sair = ' '
    while sair not in 'SN':
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
    if sair in 'Nn':
        break

print("-="*30)
print(f"Você digitou os valores {sorted(lista)}")
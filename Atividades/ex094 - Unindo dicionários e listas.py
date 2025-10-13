
temp = dict()
dados = list()

while True:
    
    temp['nome'] = input("Nome: ")
    
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = input("Sexo: [M/F] ").upper().strip()[0]
        if sexo not in 'MF':
            print("ERRO! Por favor, digite apenas M ou F")
        
    temp['sexo'] = sexo
    
    temp['idade'] = int(input("Idade: "))
    
    dados.append(temp.copy())
    
    temp.clear()
    
    sair = ' '
    
    while sair not in 'SN':
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
        if sair not in 'SN':
            print("ERRO! Por favor, digite apenas S ou N")
    if sair == 'N':
        break


print('-='*20)
print(f"A) Ao todo temos {len(dados)} pessoas cadastradas.")


soma = 0
for i in range(0, len(dados)):
    soma += dados[i]['idade']
media = soma/len(dados)

print(f"B) A média de idade é de {media} anos.")
print(f"C) As mulheres cadastradas foram ", end='')

for c in dados:
    if c['sexo'] == 'F':
        print(c['nome'], end = ' ')

print(f"\nLista de pessoas que estão acima da média: ")

for c in dados:
    if c['idade'] > media:
        for k, v in c.items():
            print(f"{k} = {v};", end=' ')
    print()

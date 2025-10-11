temp = []
dados = []

while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))
    
    media = (temp[1] + temp[2])/2
    temp.append(media)
    
    dados.append(temp[:])
    temp.clear()
    
    sair = ' '
    while sair not in 'SN':
        sair = input("Quer continuar? [S/N] ").upper().strip()[0]
    if sair == 'N':
        break

print("-="*30)

print("{:<5}{:<15}{:>3}".format("No.", "NOME", "MÉDIA"))
print("-"*50)
for c in range(0, len(dados)):
        print(f"{c:<5}{dados[c][0]:<15}{dados[c][3]:>5}")

no = -1

while True:
    print("-"*50)
    no = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if no == 999:
        break
    elif no < 0 or no > len(dados) - 1:
        print("Valor inválido, tente novamente!")
    else:
        print(f"Notas de {dados[no][0]} são {dados[no][1:3]}")
    no == 999
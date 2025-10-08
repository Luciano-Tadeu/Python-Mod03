exp = input("Digite um expressão: ")
count = 0
count2 = 0

for i in exp:
    if i == '(':
        count += 1
    elif i == ')':
        count2 += 1

if count == count2:
    print("A expressão é válida!")
else:
    print("A expressão é inválida!")
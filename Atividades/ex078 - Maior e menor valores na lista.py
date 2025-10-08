lista = []

for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
    
print(f"Você digitou os valores {lista}")

print(f"O maior valor digitado foi {max(lista)} nas posições ", end='')

for pos in range(0, len(lista)):
    if lista[pos] == max(lista):
        print(f"{pos}...", end=' ')
    

print(f"\nO menor valor digitado foi {min(lista)} nas posições ", end='')

for pos in range(0, len(lista)):
    if lista[pos] == min(lista):
        print(f"{pos}...", end=' ')
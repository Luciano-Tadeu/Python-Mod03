matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
soma3Col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-="*30)

for l in range(0, 3):
    for c in range(0, 3):
        
        print(f"[{matriz[l][c]:^5}]", end='')
        
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
            
        if l == 1 and c == 0:
            maior2Col = matriz[l][c]
        elif l == 1 and c != 0:
            if maior2Col < matriz[l][c]:
                maior2Col = matriz[l][c]
                
        if c == 2:
            soma3Col += matriz[l][c]
            
    print()
    
print("-="*30)

print(f"A soma dos valores pares é {somaPar}.")
print(f"A soma dos valores da terceira coluna é {soma3Col}")
print(f"O maior valor da segunda linha é {maior2Col}")


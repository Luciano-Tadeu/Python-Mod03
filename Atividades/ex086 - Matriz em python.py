'''matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f"Digite um valor para [{c}, {i}]: ")))

print("-="*30)
for c in matriz[0]:
    print("[{:^3}]".format(c), end='')
print()
for c in matriz[1]:
    print("[{:^3}]".format(c), end='')
print()
for c in matriz[2]:
    print("[{:^3}]".format(c), end='')''' #Minha solução
    

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-="*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='') #Solução Guanabara
    print()
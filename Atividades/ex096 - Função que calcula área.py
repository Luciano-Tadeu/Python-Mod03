print("{:^20}".format("Controle de Terrenos"))
print("-"*25)

larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

def area(l, c):
    areaC = l*c
    print(f"A área de um terreno {l}x{c} é de {areaC}m².")

area(larg, comp)
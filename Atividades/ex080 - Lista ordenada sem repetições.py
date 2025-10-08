números = list()

for c in range(0, 5):
    num = int(input("Digite um valor: "))
    
    if c == 0:
        números.append(num)
        print("Adicionado ao final da lista...")
    else:
        numIndex = -1
        for i in números:
            if num < i:
                numIndex = números.index(i)
                break

        if numIndex != -1:        
            números.insert(numIndex, num)
            print(f"Adicionado na posição {números.index(num)} da lista...")
        else:
            números.append(num)
            print("Adicionado ao final da lista...")
            
print("-="*30)
print(f"Os valores digitados em ordem foram {números}")
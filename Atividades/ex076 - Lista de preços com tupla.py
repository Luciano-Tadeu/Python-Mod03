tupla = ('Lápis', 1.75, 
         'Borracha', 2.00, 
         'Caderno', 15.90, 
         'Estojo', 25.00, 
         'Transferidor', 4.20, 
         'Compasso', 9.99, 
         'Mochila', 120.32, 
         'Canetas', 22.30, 
         'Livro', 34.90)

print("-"*30)
print("{:^30}".format("LISTAGEM DE PREÇOS"))
print("-"*30)

for c in range(0, len(tupla)):
    if  c % 2 == 0:
        nome = tupla[c]
        print("{:.<20}".format(nome), end='')
    else:
        preço = tupla[c]
        print("R$ {:>7.2f}".format(preço))
   
print("-"*30)
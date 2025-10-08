lista_Palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")

for c in range(0, len(lista_Palavras)):
    frase = lista_Palavras[c]
    print(f"Na palavra {frase} temos ", end='')
    for pos in range(0, len(frase)):
        if frase[pos] == 'A':
            print("a", end=' ')
        elif frase[pos] == 'E':
            print("e", end=' ')
        elif frase[pos] == 'I':
            print("i", end=' ')
        elif frase[pos] == 'O':
            print("o", end=' ')
        elif frase[pos] == 'U':
            print("u", end=' ')
    print(" ")    
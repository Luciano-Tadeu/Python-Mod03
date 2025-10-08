numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        numD = int(input("Digite um número inteiro entre 0 e 20: "))
        if numD <= 20 and numD >= 0:
            print("Você digitou o número {}.".format(numeros[numD]))
            break
        else:
            print("Tente novamente.", end = ' ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input("Quer outro número? [S/N] ").upper().strip()[0]
    if continuar == 'N':
        break
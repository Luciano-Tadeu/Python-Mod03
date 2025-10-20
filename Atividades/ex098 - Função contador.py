from time import sleep

def cont1():
    print("-="*25)
    print("Contagem de 1 até 10 de 1 em 1")
    c = 1
    while c <= 10:
        print(f"{c}", end=" ", flush=True)
        sleep(0.5)
        c += 1
    print("FIM!")
    
cont1()

def cont2():
    print("-="*25)
    print("Contagem de 10 até 0 de 2 em 2")
    c = 10
    while c >= 0:
        print(f"{c}", end=" ", flush=True)
        sleep(0.5)
        c -= 2
    print("FIM!")
    
cont2()

def cont3():
    print("-="*25)
    print("Agora é sua vez de personalizar a contagem!")
    ini = int(input("Inicio: "))
    fim = int(input("Fim: "))
    pas = int(input("Passo: "))
    c = ini
    
    if ini >= fim:
        print(f"Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}")
        while c >= fim:
            print(c, end=" ", flush=True)
            sleep(0.5)
            c -= abs(pas)
        print("FIM!")
    else:
        print(f"Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}")
        while c <= fim:
            print(c, end=" ", flush=True)
            sleep(0.5)
            c += abs(pas)
        print("FIM!")

cont3()
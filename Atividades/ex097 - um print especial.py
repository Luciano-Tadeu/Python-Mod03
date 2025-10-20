from random import randint

palavras = ["Luciano Tadeu", "Python", "Python não é tão dificíl assim!"]

def escreva(lst):
    ale = randint(0, 2)
    print("~"*len(lst[ale]))
    print(f"{lst[ale]:^}")
    print("~"*len(lst[ale]))

escreva(palavras)
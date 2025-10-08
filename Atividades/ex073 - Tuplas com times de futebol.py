print("-="*30)
times_brasileirao = (
    "Flamengo",      # 1º
    "Cruzeiro",      # 2º
    "Palmeiras",     # 3º
    "Mirassol",      # 4º
    "Botafogo",      # 5º
    "Bahia",          # 6º
    "São Paulo",     # 7º
    "Fluminense",    # 8º
    "RB Bragantino", # 9º
    "Grêmio",        # 10º
    "Ceará",         # 11º
    "Vasco da Gama", # 12º
    "Atlético Mineiro",
    "Corinthians",
    "Internacional",
    "Santos",
    "Juventude",
    "Vitória",
    "Fortaleza",
    "Sport"
)
print("Lista de times do Brasileirão: {}".format(times_brasileirao))
print("-="*30)
print("Os 5 primeiros colocados são {}".format(times_brasileirao[0:5]))
print("-="*30)
print("Os 4 últimos são {}".format(times_brasileirao[-4:]))
print("-="*30)
print("Os Times em ordem alfabética: {}".format(sorted(times_brasileirao)))
print("-="*30)
print("O Corithians está na {}ª posição".format(times_brasileirao.index('Corinthians') + 1))

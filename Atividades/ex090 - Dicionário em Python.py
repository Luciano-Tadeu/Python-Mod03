dados = dict()

dados['nome'] = input("Nome: ")
dados['media'] = float(input(f"Média de {dados['nome']}: "))

print("-="*25)

if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f" - {k} é igual a {v}")

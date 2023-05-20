dicionario = {}
dicionario['nome'] = str(input('nome: '))
dicionario['medi'] = float(input('Mèdia: '))
if dicionario['medi'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif 5 <= dicionario['medi'] < 7:
    dicionario['situação'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in dicionario.items():
    print(f'-- {k} é igual a {v}')

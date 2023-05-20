lista = []
dicionario = {}
soma = media = 0
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome: '))
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sex not in 'MF':
        sex = str(input('Digite apenas [M / F]: ')).strip().upper()[0]
        if sex == 'MF':
            break
    dicionario['sexo'] = sex
    resp = str(input('Deseja continuar[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta invalida Responda apenas com [S/N]: '))
    lista.append(dicionario.copy())
    if resp == 'N':
        break
media = soma / len(lista)
print('=--=' * 20)
print(f'A) Temos {len(lista)} pessoas cadastradas ')
print(f'B) A media das idades e igual a {media:5.2f}')
print('C) As mulheres cadastradas foram: ', end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f' => {k} = {v}; ', end='')
print('\n            <<< ENCERRANDO >>>         ')

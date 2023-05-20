dados = list()
coleta = list()
maior = menor = cont = 0

while True:
    coleta.append(str(input('Nome: ')))
    coleta.append(float(input('Peso:')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    cont += 1
    if len(dados) == 0:
        maior = menor = coleta[1]
    else:
        if coleta[1] > maior:
            maior = coleta[1]
        if coleta[1] < menor:
            menor = coleta[1]
    dados.append(coleta[:])
    coleta.clear()
    while resp not in 'SN':
        resp = str(input('Resposta invalida. Quer continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print('=**='*30)
print(f'Tivemos {cont} pessoas cadastradas')
print(f'O maior peso é de {maior}Kg do', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso é de {menor}Kg', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

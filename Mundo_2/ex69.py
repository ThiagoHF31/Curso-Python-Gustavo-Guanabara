contH = 0
menorMulher = 0
mais18 = 0
while True:
    print('Ξ'*20)
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F] ? ')).upper().strip()[0]
    pro = ' '
    while pro not in 'SN':
        pro = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        menorMulher += 1
    if sexo == 'M':
        contH += 1
    if idade >= 18:
        mais18 += 1
    if pro == 'N':
        break
print('——'*20)
print(f'{mais18} pessoas tem mais de 18 anos')
print(f'{contH} homens foram cadastrados ')
print(f'{menorMulher} Mulheres tem menos de 20 anos')





soma = 0
maisdemil = 0
cont = 0
menor = 0
barato = ''
while True:
    print('※'*30)
    nome = str(input('Nome do produto: ')).strip()
    pre = float(input('Preço do produto: '))
    contin = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    soma += pre
    cont += 1
    if pre >= 1000:
        maisdemil += 1
    if cont == 1:
        menor = pre
        barato = nome
    else:
        if pre < menor:
            menor = pre
            barato = nome
    if contin == 'N':
        break
print('※'*30)
print(f'O total de compras foi R$ {soma}')
print(f'Temos {maisdemil} produtos que valem mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')


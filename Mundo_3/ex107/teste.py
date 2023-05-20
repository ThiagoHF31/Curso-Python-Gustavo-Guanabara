import moeda
pre = float(input('Digite o preço: R$ '))
print(f'A metade de {pre} é {moeda.metade(pre)}')
print(f'O dobro de {pre} é {moeda.dobro(pre)}')
print(f'Aumentando 10% de {pre} temos {moeda.aumetar(pre, 10)}')
print(f'dando um desconto de 13% temos {moeda.diminuir(pre, 13)}')

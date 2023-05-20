import moeda
pre = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(pre)} é {moeda.metade(pre, True)}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.dobro(pre, True)}')
print(f'Aumentando 10% de {moeda.moeda(pre)} temos {moeda.aumetar(pre, 10, True)}')
print(f'dando um desconto de 13% temos {moeda.diminuir(pre, 13, True)}')

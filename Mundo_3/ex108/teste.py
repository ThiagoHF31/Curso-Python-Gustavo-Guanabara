import moeda
pre = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(pre)} é {moeda.moeda(moeda.metade(pre))}')
print(f'O dobro de {moeda.moeda(pre)} é {moeda.moeda(moeda.dobro(pre))}')
print(f'Aumentando 10% de {moeda.moeda(pre)} temos {moeda.moeda(moeda.aumetar(pre, 10))}')
print(f'dando um desconto de 13% temos {moeda.moeda(moeda.diminuir(pre, 13))}')

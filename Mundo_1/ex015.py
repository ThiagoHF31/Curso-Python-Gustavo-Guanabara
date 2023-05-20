dias = int(input('Quantos dias ficou alugado o carro?'))
km = float(input('Quantos km rodados?'))
c = (dias * 60) + (km * 0.15)
print('O valor a pagar e de R$ {:.2f} reais'.format(c))



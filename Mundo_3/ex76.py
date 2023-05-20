listagem = ('processador', 600,
            'placa de video', 1500,
            'gabinete', 300,
            'placa mãe', 500,
            'ssd', 400,
            'fonte', 350)
print('_' * 40)
print(f'{"Lista de Preços":^40}')
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)

lista = []
for peso in range(1, 6):
    p = float(input('Diga o {}º peso: '.format(peso)))
    lista += [p]
print('o maior peso é {}'.format(max(lista)))
print('O menor peso é {}'.format(min(lista)))

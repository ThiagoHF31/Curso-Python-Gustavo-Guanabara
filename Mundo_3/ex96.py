def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m.')


def lin():
    print('__' * 20)


lin()
p = (float(input('LARGAURA (m): ')))
lin()
p2 = (float(input('COMPRIMENTO (m): ')))
area(p, p2)
lin()

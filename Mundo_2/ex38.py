valor1 = int(input('digite um valor:'))
valor2 = int(input('digite o segundo valor'))
if valor1 > valor2:
    print('\033[34mEntre {} e {} o maior é {}'.format(valor1, valor2, valor1))
elif valor1 < valor2:
    print('\033[34mO {} e maior que o {}'.format(valor2, valor1))
else:
    print('\033[34mOs valores são iguais')

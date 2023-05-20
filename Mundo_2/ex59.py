import time
from time import sleep
r = 0
while r == 0:
    print('\033[36m=-=-=\033[m' * 20)
    print('______ Valores ______')
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    sleep(0.3)
    n3 = int(input('''Oque você deseja fazer com esses valores?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair
digite aqui: '''))
    print('\033[36m=-=-=\033[m' * 20)
    sleep(0.3)
    if n3 == 1:
        print('A soma dos valores {} + {} é \033[32m{}\033[m'.format(n1, n2, n1+n2))
    if n3 == 2:
        print('A multiplicação dos valores {} x {} e igual a \033[32m{}\033[m'.format(n1, n2, n1 * n2))
    elif n3 == 3:
        if n1 == n2:
            print('Os valores são iguais !!!')
        else:
            print('O Maior numero entre {} e {} é \033[32m{}\033[m'.format(n1, n2, max(n1, n2)))
    elif n3 == 4:
        ''
    elif n3 == 5:
        print('FINALIZANDO... Volte sempre')
        time.sleep(1)
        exit()
    elif n3 > 5:
        print('\033[31mValor invalido, digite novamente!!\033[m')


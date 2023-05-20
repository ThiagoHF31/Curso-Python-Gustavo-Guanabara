num = soma = cont = 0
while num != 999:
    num = int(input('Digite um numero [ 999 para parar ]: '))
    soma = soma + num
    cont = cont + 1
    if num == 999:
        print('A soma de todos os valores é {} e a quantidade digitada é {}'.format(soma - 999, cont))
        exit()

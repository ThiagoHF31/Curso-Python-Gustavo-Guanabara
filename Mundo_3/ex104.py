def leianumero(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# programa principal

n = leianumero('digite um numero: ')
print(f'O numero que vc digitou foi {n}')

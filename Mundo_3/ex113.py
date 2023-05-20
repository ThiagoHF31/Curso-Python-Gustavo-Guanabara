def leianumero(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiafloot(msg):
    while True:
        try:
            r = float(input(msg))
        except(ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiru não digitar esse numero.')
            return 0
        else:
            return r


# programa principal
n = leianumero('digite um numero: ')
r = leiafloot('Digite um numero real')
print(f'O numero que vc digitou foi {n} e o real foi {r}')

def aumetar(pre=0, taxa=0, formatando=False):
    """
    ==> Calcular o aumento de um determinado preço
    :param pre: Valor a ser digitado
    :param taxa: Valor em porcentagem do aumento
    :param formatando: Escolha de saida formatada ou não
    :return: Retorna um valor
    """
    res = pre + (pre * taxa/100)
    return res if formatando is False else moeda(res)


def diminuir(pre=0, taxa=0, formatando=False):
    """
    ==> Calcular o desconto de um determinado preço
    :param pre: Valor a ser digita
    :param taxa: Valor em porcetangem a ser diminuido
    :param formatando: Escolha de saida formatada ou não
    :return: Retorna um valor
    """
    res = pre - (pre * taxa/100)
    return res if formatando is False else moeda(res)


def dobro(pre=0, formatando=False):
    """
    ==> Calcular o dobro de um determinado valor
    :param pre:
    :param formatando:
    :return:
    """
    res = pre * 2
    return res if not formatando else moeda(res)


def metade(pre=0, formatando=False):
    """
    ==> Calcular a metade de um determinado valor
    :param pre:
    :param formatando:
    :return:
    """
    res = pre / 2
    return res if not formatando else moeda(res)


def moeda(pre=0, moeda='R$'):
    """
    ==> Formata o texto colocando 'R$' antes dos valores e troca ponto por virgula
    :param pre:
    :param moeda:
    :return: Retorna o valor formatado
    """
    return f'{moeda}{pre:>.2f}'.replace('.', ',')


def resumo(pre=0, taxa=10, taxar=5):
    """
    ==> Mostra todos os valores editados na tela
    :param pre:
    :param taxa:
    :param taxar:
    :return:
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(pre)}')
    print(f'Dobro do preço: \t{dobro(pre, True)}')
    print(f'Metade do preço: \t{metade(pre, True)}')
    print(f'{taxa}% de aumento: \t{aumetar(pre, taxa, True)}')
    print(f'{taxar}% de redução:  \t{diminuir(pre, taxar, True)}')
    print('-' * 30)

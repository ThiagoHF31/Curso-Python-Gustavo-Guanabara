def aumetar(pre=0, taxa=0):
    res = pre + (pre * taxa/100)
    return res


def diminuir(pre=0, taxa=0):
    res = pre - (pre * taxa/100)
    return res


def dobro(pre=0):
    res = pre * 2
    return res


def metade(pre=0):
    res = pre / 2
    return res


def moeda(pre=0, moeda='R$'):
    return f'{moeda}{pre:>8.2f}'.replace('.', ',')

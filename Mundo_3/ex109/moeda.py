def aumetar(pre=0, taxa=0, formatando=False):
    res = pre + (pre * taxa/100)
    return res if formatando is False else moeda(res)


def diminuir(pre=0, taxa=0, formatando=False):
    res = pre - (pre * taxa/100)
    return res if formatando is False else moeda(res)


def dobro(pre=0, formatando=False):
    res = pre * 2
    return res if not formatando else moeda(res)


def metade(pre=0, formatando=False):
    res = pre / 2
    return res if not formatando else moeda(res)


def moeda(pre=0, moeda='R$'):
    return f'{moeda}{pre:>.2f}'.replace('.', ',')

def aumetar(pre, taxa):
    res = pre + (pre * taxa/100)
    return res


def diminuir(pre, taxa):
    res = pre - (pre * taxa/100)
    return res


def dobro(pre):
    res = pre * 2
    return res


def metade(pre):
    res = pre / 2
    return res

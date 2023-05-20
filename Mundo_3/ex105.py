def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, idicado se deve ou não adicionar a situação
    :return: dicionário com varias infomações sobre a situaão da turma.
    """
    dicionario = dict()
    dicionario['total'] = len(nota)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'boa'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'
    return dicionario


resp = notas(9, 10, 5, 6, sit=True)
print(resp)


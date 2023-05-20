from datetime import date
ano = int(input('Qual sua data de nascimento? '))
atual = date.today().year
conta = atual - ano
if conta > 18:
    print('Você passou {} anos do tempo de se alistar, vá ate a junta militar mais proxima'.format(conta - 18))
elif conta < 18:
    print('Fique tranquilo ainda não e hora de se alistar, faltam {} anos'.format(18 - conta))
elif conta == 18:
    print('Você esta na idade de se alistar, vá ate a junta militar mais proxima')

print('...BRASIL A CIMA DE TUDO...')


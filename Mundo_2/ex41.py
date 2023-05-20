from datetime import date
ano2 = int(input('Data de nascimento:'))
atual = date.today().year
ano = atual - ano2
if ano <= 9:
    print('\033[34mNadador mirim por que tem {} anos\033[m'.format(atual - ano2))
elif ano > 9 and ano <= 14:
    print('\033[35mNadador infatil por que tem {} anos\033[m'.format(atual - ano2))
elif ano > 14 and ano <= 19:
    print('\033[32mNadador Junior por que tem {} anos\033[m'.format(atual - ano2))
elif ano > 10 and ano <= 20:
    print('\033[33mNadador Sênior por que tem {} anos\033[m'.format(atual - ano2))
elif ano > 20:
    print('\033[31mNadador Master por que tem {} anos\033[m'.format(atual - ano2))

from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 7):
    nascimento = int(input('Digite o ano de nascimento da {}º pessoa: '.format(pessoa)))
    idade = ano - nascimento
    if idade >= 18:
       totmaior += 1
    else:
        totmenor += 1
print('Ao total tivemos {} pessoas MAIORES de idade'.format(totmaior))
print('Ao total tivemos {} pessoas MENORES de idade'.format(totmenor))


resp = 'S'
lista = []
quant = soma = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero'))
    soma += num
    quant += 1
    lista += [num]
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('A média dos valores digitados é {}'.format(media))
print('O maior numero digitado foi {} e o menor foi {}'.format(max(lista), min(lista)))

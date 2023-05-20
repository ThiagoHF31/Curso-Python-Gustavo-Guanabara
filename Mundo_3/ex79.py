lista = []
while True:
    num = int(input('Digite um numero'))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!!')
    else:
        print('Valor duplicado, não adicionado!!')
    r = str(input('Quer continar [S/N]? ')).upper().strip()[0]
    if r in 'Nn':
        break
print('=-'*30)
lista.sort()
print(f'Você digitou os valores {lista}')

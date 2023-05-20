lista = []
cont = 1
while True:
    lista.append(int(input('Digite um numero: ')))
    c = str(input('Deseja continuar [ S/N ]? ')).upper().strip()[0]
    if c == 'S':
        cont += 1
    else:
        break
lista.sort(reverse=True)
print(lista)
print(f'Foram digitados {cont} numeros')
print(f'Os valores digitas em forma decrecente são {lista}')
if 5 in lista:
    print('O valor 5 esta dentro da lista!')
else:
    print('O valor 5 não esta dentro da lista!')


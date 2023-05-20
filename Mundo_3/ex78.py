lista = []
maior = []
menor = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {cont}: ')))
    print('_' * 30)
for p, valores in enumerate(lista):
    if valores == max(lista):
        maior.append(p)
    if valores == min(lista):
        menor.append(p)
print('_'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} na posição {maior} ')
print(f'O menor valor digitado foi {min(lista)} na posição {menor} ')

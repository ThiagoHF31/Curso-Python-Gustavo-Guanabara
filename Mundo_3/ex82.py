num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('\033[34mQuer continuar? [S/N] \033[m'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=+='*30)
print(f'A lista de numeros digitados é {num}')
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros impares é {impares}')

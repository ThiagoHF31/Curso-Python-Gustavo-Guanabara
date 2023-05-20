num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'Os numero digitas foram {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu pela primeira vez na posição {num.index(3)+1}º')
else:
    print('Não tem numero 3 nos numeros digitados')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


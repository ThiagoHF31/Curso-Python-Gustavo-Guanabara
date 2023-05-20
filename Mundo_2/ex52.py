num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('\033[32mPor isso ele e um numero primo\033[m')
else:
    print('\033[33mPor isso ele Não é um numero primo')

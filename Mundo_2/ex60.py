import math
r = 0
while r == 0:
    num = int(input('Digite um numero para ver seu fatorial: '))
    print('O fatorial de {}! é \033[97m{}\033[m'.format(num, math.factorial(num)))
    if num == 0:
        exit()


# n = int(input('Digite um número para calcular seu Fatorial: '))
# c = n
# f = 1
# while c > 0:
#   print('{}'.format(c), end='')
#   print(' x ' if c > 1 else ' = ', end='')
#   f *= c
#   c-= 1
# print('{}'.format(f))


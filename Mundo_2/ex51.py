print('=' * 20)
print('\033[31m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
p = int(input('Primeiro termo:'))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print('{} '.format(c), end='→ ')
print('...ACABOU...')

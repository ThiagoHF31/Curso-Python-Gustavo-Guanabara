print('_-_-_-_'* 20)
print('...\033[4mANALISADOR DE TRIÂNGULOS\033[m...')
print('_-_-_-_'* 20)
p = float(input('\033[32m digite o numero da primeria reta:\033[m'))
p2 = float(input('\033[32m numero da segunda reta:\033[m'))
p3 = float(input('\033[32m numero da terceira reta:\033[m '))
if p < p2 + p3 and p2 < p + p3 and p3 < p + p2:
    print('\033[4;33;40m Os seguimentos a cima podem forma triangulo!\033[m')
else:
    print('\033[;7;34;40mO segmentos não podem forma triangulo\033[m')

import random
from time import sleep
cont = 1
acertou = False
num = random.randint(0, 10)
print('\033[32mTENTE ADVINHA EM QUE NUMERO ESTOU PENSANDO DE 0 A 10\033[m')
print('\033[34m-==-\033[m'*20)
jogador = int(input('E AE QUAL NUMERO ESTOU PENSANDO?: '))
while jogador != num:
    jogador = int(input('digite outro numero: '))
    cont += 1
    if jogador == num:
        acertou = True
    else:
        if jogador > num:
            print('\033[36mMenos... Tente novamente\033[m')
        elif jogador < num:
            print('\033[36mMais ... Tente novamente\033[m')
print('\033[34m-==-\033[m'*20)
print('...\033[4mPROCESSANDO...\033[m')
sleep(1)
print('O numero que eu pensei foi {}, parabens por acertar'.format(num))
print('Você acertou depois de {} tentativas'.format(cont))



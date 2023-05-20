import random
from time import sleep
num = random.randint(0, 5)
print('TENTE ADVINHA EM QUE NUMERO ESTOU PENSANDO DE 0 A 5')
print('-==-'*20)
jogador = int(input('E AE QUAL NUMERO ESTOU PENSANDO?: '))
print('-==-'*20)
print('PROCESSANDO...')
sleep(2)

print('O numero que você chutou foi {} eu pensei no {}'.format(jogador, num))
if num == jogador:
    print('Você acertou mizeravel')
else:
    print('Errouuu, mais sorte na proxima')


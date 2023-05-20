import random
import time
print('\033[4;36m*=*\033[m' * 20)
print('VAMOS JOGAR')
print('''\033[4mESCOLHA UM E TENTE ME VENCER:\033[m 
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] tesoura''')
op = int(input('Qual é sua jogada? '))
if op >= 3:
    print('JOGADA ERRADA, tente de novo')
    exit()
print('\033[34mJO\033[m')
time.sleep(1)
print('\033[34mKen\033[m')
time.sleep(1)
print('\033[34mPO\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('\033[35m -=\033[m' * 15)
print('O computador jogou {}'.format(itens[computador]).upper())
print('Jogador jogou {}'.format(itens[op]).upper())
print('\033[35m-=\033[m' * 15)
if computador == 0:
    if op == 0:
        print('\033[97mEMPATE\033[m')
    elif op == 1:
        print('\033[32m Jogador Venceu\033[m')
    elif op == 2:
        print('\033[31mJogador Perdeu\033[m')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if op == 0:
        print('\033[31mJogador Perdeu\033[m')
    elif op == 1:
        print('\033[97m EMPATE\033[m')
    elif op == 2:
        print('\033[32m Jogador venceu\033[m')
elif computador == 2:
    if op == 0:
        print('\033[32m Jogador Venceu\033[m')
    elif op == 1:
        print('\033[31mJogador Perdeu\033[m')
    elif op == 2:
        print('\033[97m EMPATE\033[m')



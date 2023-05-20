import random
computador = random.randint(1, 10)
cont = 0
while True:
    print('...'*20)
    print('JOGO DO IMPAR OU PAR')
    print('...'*20)
    jogador = int(input('Digite um numero: '))
    escolha = str(input('Par ou Impar [P/I]? ')).upper().strip()[0]
    soma = jogador + computador
    par = soma % 2
    if escolha == 'P' and par == 0:
        print('\033[34mDeu Par, ganhou\033[m')
    elif escolha == 'I' and par == 1:
        print('\033[34mDeu impar, ganhou\033[m')
    elif escolha == 'P' and par == 1:
        print('\033[31mDeu impar, perdeu\033[m')
        break
    elif escolha == 'I' and par == 0:
        print('\033[31mDeu par, perdeu\033[m')
        break
    cont += 1
print('=-'*20)
print(f'\033[34mVocê acertou {cont} vezes seguidas ')

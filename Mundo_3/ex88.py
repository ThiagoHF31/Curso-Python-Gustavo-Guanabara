from random import randint
from time import sleep
lista = list()
jogos = list()
print('=' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('\033[34m=_=' * 3, f'Sorteando {quant} Jogos', '=_=' * 3)
sleep(1)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'\033[mjogo {i+1}: {l}')
print(f'{"...BOA SORTE...":^30}')

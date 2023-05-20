import random
sorteado = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
            random.randint(0, 10),)
print('Os valores foram : ', end=' ')
for n in sorteado:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(sorteado)}')
print(f'O menor valor sorteado foi {min(sorteado)}')





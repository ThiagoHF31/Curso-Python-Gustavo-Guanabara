print('=' * 20)
print('\033[31m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
primeiro = int(input('digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
total = 0
cont = 1
termo = primeiro
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    mais = int(input('\nQuantos termos a mais gostaria de ver ?: '))
print('FIM')

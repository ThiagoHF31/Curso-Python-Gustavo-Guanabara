print('=' * 20)
print('\033[31m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
primeiro = int(input('digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
quantidade = int(input('Quantos termos você dejesa que sejam exibidos? '))
cont = 1
termo = primeiro
while cont <= quantidade:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

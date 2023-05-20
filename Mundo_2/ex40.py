nota1 = float(input('nota 1:'))
nota2 = float(input('nota 2:'))
cal = (nota1 + nota2) / 2
if cal < 5:
    print('REPROVADO')
elif cal < 7 or cal == 5:
    print('Recuperação')
elif cal >= 7:
    print('APROVADO')
print('Sua media foi {:.1f}'.format(cal))

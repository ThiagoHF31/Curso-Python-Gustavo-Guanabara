s = float(input('\033[34mQual seu salario ?\033[m'))
v1 = s * 1.10
v2 = s * 1.15
if s >= 1250:
    print('Seu salario foi de R$ {:.2f} para R$ {:.2f}'.format(s, v1))
else:
    print('Seu salario foi de R$ {:.2f} para R$ {:.2f}'.format(s, v2))

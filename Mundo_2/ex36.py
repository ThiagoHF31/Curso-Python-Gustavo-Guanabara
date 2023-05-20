valor1 = float(input('Qual valor da casa? '))
valor2 = float(input('Quanto você ganha por mês? '))
valor3 = float(input('Em quantos anos pretende pagar'))
meses = valor3 * 12
parcelas = valor1 / meses
if parcelas > valor2 * 30 / 100:
    print('\033[31mImprestimo recusado\033[m')
elif parcelas < valor2 * 1.30:
    print('\033[32m...Imprestimo aceito...\033[m')
    print('Em {} anos temos {} meses e as parcelas ficaram de R${:.2f} mensais'.format(valor3, meses, parcelas))


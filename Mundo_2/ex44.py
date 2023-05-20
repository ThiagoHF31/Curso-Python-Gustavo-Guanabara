print(f'{"LOJAS THIAGOHF":=^40}')
pre = float(input('PREÇO DAS COMPRAS: '))
print('''ESCOLHA A FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção ? '))
if op == 1:
    total = pre - (pre * 10 / 100)
elif op == 2:
    total = pre - (pre * 5 / 100)
elif op == 3:
    total = pre
    parcela = pre / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif op == 4:
    total = pre + (pre * 20 / 100)
    totaldparce = int(input('Quantas parcelas são? '))
    parcela = total / totaldparce
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totaldparce, parcela))
else:
    total = pre
    print('\033[31mOPÇÃO INVALIDA, tente novamente.\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pre, total))





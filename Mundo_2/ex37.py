num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Coverter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} Covertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} Covertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção ivalida, tente de novo')

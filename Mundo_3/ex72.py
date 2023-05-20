num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze')
num1 = ('quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
soma = num + num1
pos = ' '
pos = int(input('Digite um valor entre 0 a 20: '))
while True:
    if pos > 21 or pos < 0:
        pos = int(input('Digite um valor entre 0 a 20: '))
    else:
        break
print(f'O valor digitado foi {soma[pos]}')

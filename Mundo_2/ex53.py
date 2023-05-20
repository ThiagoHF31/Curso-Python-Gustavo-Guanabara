frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
inverso = ''
for letra in range(len(junta)-1, -1, -1):
    inverso += junta[letra]
if inverso == junta:
    print('Temos um palídromo !')
else:
    print('A frase digitada não é um palidromo!')

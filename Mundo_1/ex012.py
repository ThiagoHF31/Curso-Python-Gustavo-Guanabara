p = float(input('Qual é o preço do produto R$ ?:'))
d = (p * (5/100))
r = (p-d)
print('O produto que valia {} com 5% de desconto fica valendo {:.2f}:'.format(p, r))

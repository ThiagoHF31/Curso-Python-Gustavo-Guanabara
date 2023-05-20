p = float(input('Qual é o salario do funcionario R$?:'))
c = (p * 15/100)
r = (p + c)
print('O salario do funcionario de {:.2f} com um aumento de 15% fica {:.2f}'.format(p, r))

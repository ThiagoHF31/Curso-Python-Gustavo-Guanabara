vel = float(input('digite a velocidade do carro: '))
multa = (vel-80)*7
if vel>80:
    print('Você foi multado por exeder o limite de velocidade da via!')
    print('VALOR A PAGAR R$ {}'.format(multa))
else:
    print('Sua velocidade esta dentro do permitido, parabens!')
print('tenha um bom dia, dirija com segurança!')

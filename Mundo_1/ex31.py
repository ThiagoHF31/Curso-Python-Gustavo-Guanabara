distacia = float(input('Digite a distancia da sua viagem em KM:'))
c = (distacia*0.45)
c1 = (distacia*0.50)
if distacia>200:
    print('O valor da viagem será R$ {}'.format(c))
else:
    print('O valor da viagem será R$ {}'.format(c1))

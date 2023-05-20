l1 = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
area = (l1*a)
print('Sua parede tem dimensão {}X{} e sua area e de {} m'.format(l1, a, area))
print('Pra pintar essa parede você vai precisar de {} litros de tinta!'.format(area/2))



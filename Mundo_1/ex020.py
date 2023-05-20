import random
n1 = input('primeiro nome')
n2 = input('segundo nome')
n3 = input('terceiro nome')
n4 = input('quarto nome')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem de apresentação sera')
print(lista)

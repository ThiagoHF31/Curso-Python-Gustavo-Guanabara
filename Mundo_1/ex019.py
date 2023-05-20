import random
n1 = input('Nome do primeiro aluno:')
n2 = input('nome do segundo aluno:')
n3 = input('nome do terceiro aluno:')
n4 = input('nome do quarto aluno')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O sorteado da vez sera o {}'.format(escolhido))


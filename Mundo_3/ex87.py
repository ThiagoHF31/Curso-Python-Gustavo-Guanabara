matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = 0
print('=*+=' * 15)
print(f'{"Gerador de matrix":^58}')
print('=*+=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=*+='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print('=+*=' * 20)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matrix[l][2]
print(f'A soma dos valores da terceira coluna e {scol}')
print(f'O maior numero da terceira colua é {max(matrix[1])}')

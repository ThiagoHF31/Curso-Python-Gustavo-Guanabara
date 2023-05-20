matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    print()

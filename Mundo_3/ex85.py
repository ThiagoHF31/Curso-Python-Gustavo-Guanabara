lista = [[], []]
for c in range(1, 8):
    v = int(input(f'digite o {c}º valor: '))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)
print(f'Os valores Pares foram {sorted(lista[0])}')
print(f'Os valores Impares foram{sorted(lista[1])}')

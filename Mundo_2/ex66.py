cont = 0
soma = 0
while True:
    nu = int(input('Digite um valor ou (999 para parar):  '))
    if nu == 999:
        break
    soma += nu
    cont += 1
print(f'A soma dos {cont} valores será {soma}')

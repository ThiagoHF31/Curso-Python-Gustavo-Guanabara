cont = 0
while True:
    nu = int(input('Deseja ver qual tabuada? '))
    if nu < 0:
        break
    print('~~'*20)
    for c in range(0, 11):
        print(f'{nu} x {c} = {nu*c}')
print('Fim da Tabuada, volte sempre...')

        


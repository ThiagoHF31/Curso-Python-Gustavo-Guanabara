ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    nota4 = float(input('Nota 4: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    ficha.append([nome, [nota1, nota2, nota3, nota4], [media]])
    resp = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
print('==' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<14}{a[2]}')
while True:
    print('---'* 20)
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('... VOLTE SEMPRE....')

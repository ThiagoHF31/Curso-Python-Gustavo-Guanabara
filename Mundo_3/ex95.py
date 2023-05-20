jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partia {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro!! digite apenas [S/N]: ')
    if resp == 'N':
        break
print('**' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('**' * 30)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('**' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!! Não existe jogador com código {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No {i+1}º jogo fez {g} gols.')
    print('##' * 30)
print('    !!<<< VOLTE SEMPRE >>>!!')

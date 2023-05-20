dic = dict()
partidas = list()
total = 0
nome = str(input('Nome do jogador: '))
dic['nomes'] = nome
partida = int(input(f'Quantas partidas {dic["nomes"]} jogou? '))
for c in range(0, partida):
    quant = int(input(f'    Quantos gols na {c + 1}º partida: '))
    partidas.append(quant)
    total += quant
dic['gols'] = partidas[:]
print('==' * 20)
print(dic)
print('=-' * 30)
print(f'O nome é \033[35m{nome}\033[m')
print(f'A quantidade de gol desse jogador foi de \033[34m{total}\033[m gols')
print('=-' * 30)


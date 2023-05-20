import random
import time
from operator import itemgetter
dic = dict()
ranking = list()
dic['jogador1'] = random.randint(0, 6)
dic['jogador2'] = random.randint(0, 6)
dic['jogador3'] = random.randint(0, 6)
dic['jogador4'] = random.randint(0, 6)
for i, n in dic.items():
    time.sleep(1)
    print(f'O {i} recebeu {n} no dado')
print('........ Ranking........')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'    \033[34m{i+1}º lugar: {v[0]} com {v[1]}.')

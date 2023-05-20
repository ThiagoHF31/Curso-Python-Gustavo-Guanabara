import time


def analise(* num):
    print('==' * 25)
    print('\033[36mAnalisando valores passados...\033[m')
    time.sleep(1)
    print(f'{num} foram informados {len(num)} valores')
    print(f'O maior valor foi {max(num)}')
    print('==' * 25)
    time.sleep(1)


analise(3, 4, 6, 8, 9)
analise(5, 6, 7)
analise(1, 2)
analise(0)

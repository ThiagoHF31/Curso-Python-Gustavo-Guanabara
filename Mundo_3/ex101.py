import datetime

while True:
    def voto(n=0):
        idade = datetime.date.today().year - num
        if 18 <= idade < 64:
            print(f'Você tem {idade} anos. Seu voto e obrigatorio!!')
        if 18 > idade > 14:
            print(f'Você tem {idade} anos. Seu voto é opcinal!')
        if idade >= 65:
            print(f'Você tem {idade} anos. Seu voto e opcional')
        if idade < 14:
            print(f'Você tem {idade} anos. Não precisa votar ainda!')


    print('_' * 30)
    num = int(input('Em que ano vc nasceu? [digite 999 para sair] '))
    if num == 999:
        break
    voto(num)
print('Acabou!')

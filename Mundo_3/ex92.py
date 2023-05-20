dic = {}
dic['nome'] = str(input('Nome: '))
da = int(input('Ano de nascimento: '))
cal = 2022 - da
dic['idade'] = cal
cart = int(input('Carteira de trabalho [se nao tiver coloque 0]: '))
dic['carteira'] = cart
if cart > 0:
    contra = int(input('Ano de contratação'))
    dic['ano de contrato'] = contra
    dic['salario'] = int(input('Seu salario R$: '))
    soma = contra + 35
    print('==' * 20)
    print(f'Você so vai aposentar com {dic["idade"] + (soma - da)} anos de idade')
    print('==' * 20)
    print(f'O numero da carteira de trabalho é {cart}')
    print('==' * 20)
    print(f'O Salario tem valor valor {dic["salario"]}')
    print('==' * 20)
print('==' * 20)
print(f'O nome é {dic["nome"]}')
print('==' * 20)
print(f'A idade é {cal}')
print('==' * 20)
print(dic)

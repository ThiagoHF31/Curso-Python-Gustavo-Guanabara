altura = float(input('Qual sua altura? '))
peso = float(input('qual seu peso? '))
cal = peso / altura**2
print(cal)
if cal <= 18.5:
    print('\033[35mAbaixo do peso')
elif cal > 18.5 and cal <= 25:
    print('\033[32mPeso ideal')
elif cal > 25 and cal <= 30:
    print('\033[34mSobre peso')
elif cal > 30 and cal < 40:
    print('\033[33mObesidade')
elif cal > 40:
    print('\033[31mObesidade morbida')

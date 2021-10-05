print('1.hipotenusa 2.cateto')
seletor_calculo = input('selecione o que você deseja calcular: ')

if seletor_calculo == '1':
    b = float(input('informe o primeiro cateto: '))
    c = float(input('informe o segundo cateto: '))
    a = round(((b ** 2) + (c ** 2)) ** (1/2))
    print(f'sua hipotenusa é igual a {a} Um.')

if seletor_calculo == '2':
    a = float(input('informe a hipotenusa: '))
    b = float(input('informe o cateto: '))
    c = round(((a ** 2) - (b ** 2)) ** (1/2))
    print(f'seu cateto é igual a {c} Um.')

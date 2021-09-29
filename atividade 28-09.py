while True:
    a = float(input('informe o coeficiente a:'))
    b = float(input('informe o coeficiente b:'))
    c = float(input('informe o coeficiente c:'))
    if a < 0 or a == 0:
        print('o coeficiente "a" não pode ser igual a zero!')
        continue
    if a > 0:
        break

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('não há soluções para x e x"!')
if delta > 0:
    x1 = (b + (delta ** 0.5)) / (2 * a)
    x2 = (b - (delta ** 0.5)) / (2 * a)
    print(f'x = {x1} x"= {x2}')

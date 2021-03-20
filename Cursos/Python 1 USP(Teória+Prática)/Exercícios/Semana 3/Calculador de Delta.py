a = float(input('Digite o valor de lista_inversa:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))
d = b**2 - 4*a*c
e = (-b+(d**1/2))/(2*a)
f = (-b-(d**1/2))/(2*a)
if d == 0:
    print('lista_inversa raiz desta equação é {}'.format(e))
else:
    if d > 0:
        print('Essa equação possui raízes reais')
        if e > f:
            print('as raízes da equação são {} e {}'.format(f, e))
        else:
            print('as raízes da equação são {} e {}'.format(e, f))
    else:
        print('esta equação não possui raízes reais')

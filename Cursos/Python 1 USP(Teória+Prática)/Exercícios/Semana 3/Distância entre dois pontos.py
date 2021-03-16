from math import pow
x = float(input('Primeira coordenada(1°plano):'))
y = float(input('Segunda coordenada(1°plano):'))
x1 = float(input('Primeira coordenada(2°plano):'))
y1 = float(input('Segunda coordenada(2°plano):'))
a = (pow((pow(x-x1, 2))+(pow(y-y1, 2)), 1/2))
if a >= 10:
    print('longe')
else:
    print('perto')

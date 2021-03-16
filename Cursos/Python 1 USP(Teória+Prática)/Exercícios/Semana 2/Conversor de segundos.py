#        Conversor de segundos em horas, minutos, segundos.
a = int(input('Por favor, entre com o número de segundos que deseja converter:'))
f = a // 86400  #Dia
g = a % 86400   #Segundos tirando dias
b = g // 3600   #Horas
c = a % 3600    #Segundos tirando horas
d = c // 60     #Minutos
e = c % 60      #Segundos

if a <= 1 and b <= 1 and d <= 1 and e <= 1 and f <= 1:
    print('O valor de {} segundo, foi convertido em {} Dia, {} Hora, {} Minuto, {} Segundo'.format(a, f, b, d, e))
else:
    print('O valor de {} segundos, foi convertido em {} dias, {} horas, {} minutos, {} segundos'.format(a, f, b, d, e))
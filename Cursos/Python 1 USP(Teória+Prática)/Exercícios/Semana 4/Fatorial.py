#Farorial
fator = int(input('Qual o valor a virar fatorial?'))
fatorial = 1
i = 2
if fator < 0:
    fator = 0
while i <= fator:
    fatorial = fatorial * i
    i = i + 1
print(fatorial)

a = int(input('Digite um número e se for divisível por 3 e 5, vc receberá BuzzFizz:'))
if a % 3 == 0 and a % 5 == 0:
    print('FizzBuzz')
else:
    print(a)

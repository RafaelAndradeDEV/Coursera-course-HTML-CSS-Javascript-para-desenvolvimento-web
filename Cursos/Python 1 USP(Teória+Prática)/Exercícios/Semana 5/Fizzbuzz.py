def fizzbuzz(x):
    y = 0
    x = int(x)
    a = 1
    potencia = 2
    e = 10
    while y < x:
        y = y + 1
        if y == e and y >= 10:
            if y != x / 5:
                potencia = potencia + 2
                e = e + 5
        if x / 3 == y and x / 5 != y:
            a = 'Fizz'
        if x / 3 != y and x / 5 == y:
            a = 'Buzz'
        if x / 3 == y and x / 5 == (y - potencia):
            a = 'FizzBuzz'
            y = x + 1
        if a != 'Fizz' and a != 'Buzz' and a != 'FizzBuzz':
            if x / 3 != y and x / 5 != y:
                a = x
    return a
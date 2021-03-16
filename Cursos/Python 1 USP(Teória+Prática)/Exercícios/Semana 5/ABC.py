def vogal(x):
    import random
    vogal = str
    consoante = str
    x = x.lower()
    a = 1
    b = 1
    g = bool
    while a == b:
        vogal = random.choice(['a', 'e', 'i', 'o', 'u'])
        if x == vogal:
            g = True
            a = 2
        consoante = random.choice(['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'h', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])
        if x == consoante:
            g = False
            a = 2
    return g
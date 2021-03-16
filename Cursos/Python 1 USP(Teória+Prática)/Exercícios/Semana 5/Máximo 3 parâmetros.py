def maximo(x, y, z):
    a = 1
    if x >= y >= z or x >= z >= y:
        a = x
    if y >= x >= z or y >= z >= x:
        a = y
    if z >= y >= x or z >= x >= y:
        a = z
    return a
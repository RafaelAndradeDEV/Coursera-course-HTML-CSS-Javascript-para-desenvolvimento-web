def remove_repetidos(lista):
    a = 0
    lista_certa = []
    lista.sort()
    for x in lista:
        if a == x:
            x = []
        else:
            a = x
            lista_certa += [x]
    return lista_certa

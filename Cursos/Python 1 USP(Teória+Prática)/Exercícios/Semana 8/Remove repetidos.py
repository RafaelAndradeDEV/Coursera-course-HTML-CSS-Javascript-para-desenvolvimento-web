lista = [3,5,6,7,3,3,8]

def remove_repetidos(lista):
  lista_organizada = []
  delete = int
  for x in lista:
    if x == delete:
      del lista[x]
    else:
      lista_organizada.append(x)
    delete = x
    lista_organizada.sort()
  return lista_organizada

print(remove_repetidos(lista))
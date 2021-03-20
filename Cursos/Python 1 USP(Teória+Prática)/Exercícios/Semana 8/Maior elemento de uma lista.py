def  maior_elemento(lista):
  a = -10 ** 1001
  for x in lista:
    if a < x:
      a = x
  return a

lista = [-90, -27, -12]
print(maior_elemento(lista))



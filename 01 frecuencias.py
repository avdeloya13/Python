"""
Frecuencias.
"""

def frecuencia_A(arreglo):
  '''Cuenta cuántas veces aparece cada elemento del arreglo'''
  arreglo.sort()
  long = len(arreglo)
  i = 1
  for i in range(long):
    j = int(i)-1
    if(arreglo[i] != arreglo[j]):
      d = {arreglo[i]: arreglo.count(arreglo[i])}
      print(d)


def cuenta(arreglo, numero):
  '''Auxiliar que cuenta el numero de apariciones de un 
elemento en un arreglo'''
  long = len(arreglo)
  i = 0
  total = 0
  for i in range(long):
    if(arreglo[i] == numero):
      total = int(total)+1
  return total


def frecuencia_B(arreglo):
  '''Cuenta cuántas veces aparece cada elemento del arreglo
  Usando diccionarios'''
  long = len(arreglo)
  i = 1
  d ={}
  for i in range(long):  
    d[arreglo[i]] = cuenta(arreglo,arreglo[i])
    i = int(i)+1
  return d

prueba = [3,4,7,4,3,7,4,9,9,8,1,1,2,3] 
print(frecuencia_B(prueba))

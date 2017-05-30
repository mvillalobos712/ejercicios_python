# Descripcion: Programa que devuelve una lista que contiene solo los elementos que son comunes entre dos listas de distintos tamanos generadas aleatoriamente (sin duplicados)
# Entrada: Listas generadas aleatoriamente por el programa
# Salida:  Lista de elementos comunes entre ambas listas
# Autor:   MVILLALOBOS712
# Fecha:  30.05.2017
# Version: 2.0
#Plataforma: Python v2.7

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]                                                               #declara una lista a llena ya con los elementos
b = []                                                                                                                   #declara una lista vacia para ser llenada
for i in a:                                                                                                             #revisa cada numero en la lista a
 if i<5:                                                                                                                 #condicional, si el numero es menor a 5
  b.append(i)                                                                                                      #el numero se carga en la lista b
print b                                                                                         #imprime la lista b con los numeros menores a cinco

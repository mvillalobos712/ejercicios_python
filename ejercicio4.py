# Descripcion: preguntar al usuario por el numero que necesita sus divisores
# Entrada: numero para dividir
# Salida:  numeros que dividen exactamente al que da el usuario
# Autor:   MVILLALOBOS712
# Fecha:  31.05.2017
# Version: 2.0
#Plataforma: Python 2.7

numero = input("cual es el numero para saber sus divisores? ")
numero = int(numero)
divisores = []
lista = list(range(1,numero))
for i in lista:
 if numero%i== 0:
  divisores.append(i)
print divisores


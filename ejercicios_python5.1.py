#descripcion: programa donde se le pregunte al usuario por un numero  e imprima los divisores de ese numero
#entrada: preguntar al usuario por un numero 
#salida: numero divisores de el numero dado por el usuario
#autor: mvillalobos
#fecha :12/07/2017
#version:2.0
#plataforma: python v2.7

x  = int(input("ingrese numero:"))
for i in range(1,x + 1):
 if x%i==0:
 print(i)

#!/usr/bin/python3

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

subproblema = None
tiendas = set()

for claveValor in sys.stdin:
    cliente, tienda = claveValor.strip().split("\t", 1)

    if subproblema == None:
        subproblema = cliente

    if subproblema == cliente:
       tiendas.add(tienda)	

    else:
      tiendas.add(tienda)	

      print("%s\t%s" % (subproblema, tiendas))

      subproblema = cliente
      tiendas = set()
      tiendas.add(tienda)




print("%s\t%s" % (subproblema, tiendas))
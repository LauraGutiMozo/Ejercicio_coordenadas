print("EJERCICIO 1" )

import sys

from numpy import vectorize		
sys.path.append("C:\Users\LAURA\Documents\GitHub\Ejercicio_coordenadas\Punto.py")
sys.path.append("C:\Users\LAURA\Documents\GitHub\Ejercicio_coordenadas\rectangulo.py")

from Punto import punto

if "__name__==__main__":
    print(punto())
    print (punto.cuadrante())
    print(punto.vector())
    print(punto.distancia())

from rectangulo import rectangulo
if "__name__==__main__":
    print (rectangulo.base())
    print (rectangulo.altura())
    print(rectangulo.area())
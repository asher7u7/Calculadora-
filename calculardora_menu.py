# Calculadora básica con menú

from math import log

# input
bandera = False
x = float(input("ingrese el valor de x: "))
y = float(input("ingrese el valor de y: "))

print("dame la opcion que deseas realizar: \n")

#Se despliega meú para seleccionar la opcion que desea realizar
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")

opcion = int(input("elige la opción: "))

# processing 
if opcion == 1:
    z = x + y
    print(x," + ",y)
elif opcion == 2:
    z = x - y
    print(x," - ", y)
elif opcion == 3:
    z = x * y
    print(x,"*",y)
elif opcion == 4 and y !=0:
    z = x/y
    print(x,"/",y)
elif opcion == 4 and y == 0:
    print("El denominador es igual a Cero")
    print("NO se puede realizar la división")
    bandera = True
elif opcion == 5:
    z = pow(x,y)
    print(x,"^",y)
elif opcion == 6 and x>0:
    z = log(x)
    print("Logaritmo de ", x)
elif opcion == 6 and x<=0:
    print("NO se puede calcular el logaritmo.")
    bandera = True
else:
    print("Opción no válida")

# Se escribe el resultado con otra condicion
if opcion < 7 and bandera == False:
    print("Resultado = ",z)

# FIN
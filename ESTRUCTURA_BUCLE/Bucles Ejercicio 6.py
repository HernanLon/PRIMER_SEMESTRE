#Escribir un programa que pida al usuario un número entero
#y muestre por pantalla un triángulo rectángulo como el de más abajo,
#de altura el número introducido.

#Solución 1
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

#Solución 2
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))

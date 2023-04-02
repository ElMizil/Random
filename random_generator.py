import random

print("Cuantas opciones son?")
n = int(input())
opciones = []
for i in range(0,n):
    print("Ingrese opcion")
    x = input()
    opciones.append(x)
num = random.randint(0,n-1)
print(opciones[num])


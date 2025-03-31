import random

num=random.randint(5,15)
arreglo = []
while len(arreglo) < num:
    numero = random.randint(1, 100)  
    tupla1 = (numero,)
    if tupla1 in arreglo:
        print(f"El número {numero} ya se encuentra en el arreglo como tupla {tupla1}.")
    else:
        arreglo.append(tupla1)  

print("Arreglo generado con tuplas:", arreglo)


cantidad=random.randint(5,15)
def sumimpar(tupla2):
    for i in range(cantidad):
        vlr1=random.randint(1,100)
    return sum(vlr for vlr in tupla2 if numero % 2 != 0)

def promimpares(tupla2):
    impares = [numero for numero in tupla2 if numero % 2 != 0]
    if impares:
        return sum(impares) / len(impares)
    else:
        return sumimpar 

tupla_numeros = (12, 15, 7, 8, 21, 10, 33)
suma = sumimpar(tupla_numeros)
promedio = promimpares(tupla_numeros)
print("Tupla:", tupla_numeros)
print("Suma de los números impares:", suma)
print("Promedio de los números impares:", promedio)


import random
import math

def generar_lista_con_tuplas(n):
    lista = []
    for _ in range(n):
        numero = random.randint(2, 15)  
        factorial = math.factorial(numero)  
        lista.append((numero, factorial))  
    return lista

print("Lista generada con tuplas:")
for numero, factorial in resultado:
    print(f"Número: {numero}, Factorial: {factorial}")

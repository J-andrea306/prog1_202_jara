lista=[]
lista=[1,2,3]
tupla=(12,13,14,15)
print(type(tupla))
print(tupla[0])
print(tupla[-1])
for dato in tupla:
    print(dato)
    
tupla=tupla+(16,)
print(tupla)

#declare una tupla y llenela con numeros aleatorios entre 5 y 15 numeros y los numeros con los que se llene deben ser de 1 a 100. use concadenacion

import random

tupla=()
cantidad=random.randint(5,15)
for i in range(cantidad):
    num=random.randint(1,100)
    tupla=tupla+(num,)
    
print(tupla)


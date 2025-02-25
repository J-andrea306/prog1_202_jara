print("responda si o no")
rta=input("la via Silvania esta congestionada?")
if rta=="si":
 print("Tomar via por Sibate")
elif rta=="no":
 print("Tomar via por Silvania")
else:
 print("Busque una opcion diferente")
 num=int(input("Ingrese el numero"))
if num%2==0:
 print("par")
else:
 print("impar")


 #Determinar si es positivo negativo o neutro
numero=int(input("Ingrese el numero"))
if numero>0:
 print("numero es positivo")
elif numero<0:
 print("el numero es negativo")
else:
 print("el numero es neutro")

 #Solicite dos numeros si es acendente,desendente o iguales
numero=int(input("Ingrese el numero"))
numero2=int(input("Ingrese el numero"))
if numero>numero2:
 print("el orden es ascendente")
elif numero<numero2:
 print("el orden es descendente")
else:
 print("los dos numeros son iguales")

#Si el primero es mayor dividalos,si el segundo es menor multipliquelos si son iguales sumelos


numero=int(input("Ingrese el numero"))
numero2=int(input("Ingrese el numero"))
if numero>numero2:
 rest=int(input(numero/numero2))
 print("el resultado es",rest)
elif numero<numero2:
 rest2=int(input(numero*numero2))
 print("el resultado es",rest2)
else:
 rest3=int(input(numero+numero2))
 print("el resultado es",rest3)

#Si la edad de protecion del estado es patra niños y adultos
edad=int(input("Ingrese la edad"))
if edad<=18 or edad >=60:
 print("si tiene proteccion")
else:
 print("no tiene proteccion")

#Ejercicio 6
numero=int(input("Ingrese el numero"))
num2=int(input("Ingrese el numero"))
if numero/num2 == numero//num2:
 print(f"{num2}es un factor de{numero}")
elif num2/numero == num2//numero:
 print(f"{numero}es un factor de{num2}")
else:
 print("Ninguno de los dos es factor del otro")

#Ejercicio 7
import math
a= float(input("a"))
b= float(input("b"))
c=float(input("C"))
if a ==0:
 print("No es una ecuacion cuadratica")
else:
 d= b**2 - 4*a*c
 if d<0:
 print("No tiene soluciuon")
 else:
 print(f"x1={(-b+math.sqrt(d))/(2*a)}")
 print(f"x2={(-b-math.sqrt(d))/(2*a)}")
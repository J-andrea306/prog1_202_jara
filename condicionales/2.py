1

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 <= num2 and num1 <= num3:
 medio = num1
elif num2 <= num1 and num2 <= num3:
 medio = num2
else:
 medio = num3

print("El número es, medio")

2

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 == num2 == num3:
 print("Los tres números son iguales.")
elif num1 == num2 or num1 == num3 or num2 == num3:
 print("Hay dos números iguales.")
else:
 print("Los tres números son distintos.")

4
calificar(nota):
 if nota < 0 or nota > 10:
 print ("Nota fuera de rango")
 elif nota < 3:
 print ("Insuficiente")
 elif nota < 5:
 print ("Suficiente")
 elif nota < 7:
 print ("Bien")
 elif nota < 9:
 print ("Notable")
 else:
 print ("Sobresaliente")

try:
 nota = float(input("Introduce una nota de 0 a 10: "))
resultado = calificar(nota)
 print("La calificación es”,resultado)
except ValueError:
 print("Por favor, introduce un número válido.")

 
diferencia = (“fecha actual”) – (“fecha_usuario”)

if diferencia de dias > 0:
 print("Han pasado (diferencia de días) días desde la fecha ingresada.")
elif diferencia de dias < 0:
 print("Faltan (diferencia de días) días para llegar a la fecha ingresada.")
else:
 print("La fecha ingresada es hoy.")


12
 hora_actual = input("Introduce la hora actual en formato HH:MM:SS: ")

hora_actual_dt = datetime.datetime.strptime(hora_actual, "%H:%M:%S")

hora_futura_dt = hora_actual_dt + datetime.timedelta(seconds=1)

print("La hora dentro de un segundo será:", hora_futura_dt.time())



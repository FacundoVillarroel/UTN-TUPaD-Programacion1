# Ejercicio 1
print("Ejercicio 1")
print("Hola Mundo!")

# Ejercicio 2
print("Ejercicio 2")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
print("Ejercicio 3")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
print("Ejercicio 4")
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"Area: {area}")
print(f"Perímetro: {perimetro}")

# Ejercicio 5
print("Ejercicio 5")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
print("Ejercicio 6")
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Ejercicio 7
print("Ejercicio 7")
num1 = int(input("Ingrese el primer numero (distinto de 0): "))
num2 = int(input("Ingrese el segundo numero (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# Ejercicio 8
print("Ejercicio 8")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es: {imc}")

# Ejercicio 9
print("Ejercicio 9")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F")

# Ejercicio 10
print("Ejercicio 10")
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}")

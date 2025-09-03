# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

print("Ejercicio 1")

for i in range(101):
  print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

print("Ejercicio 2")

num = input("Ingrese un número entero: ")         
print("El número ingresado tiene", len(num), "dígitos.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

print("Ejercicio 3")

num1= int(input("Ingrese el primer número entero: "))
num2= int(input("Ingrese el segundo número entero: "))
suma=0
if num1 < num2:   # Asegurarse de que num1 es menor que num2
  for i in range(num1+1, num2):
    suma += i
elif num1 > num2: # Si num1 es mayor que num2, intercambiarlos
  for i in range(num2+1, num1):
    suma += i
print("La suma de los números entre", num1, "y", num2, "es:", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

print("Ejercicio 4")

num = int(input("Ingrese un número entero positivo: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese otro número entero positivo (o 0 para terminar): "))

print("La suma total es:", suma)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
print("Ejercicio 5")

cont = 0
num = 10 # diferente a numAleatorio para entrar al while
numAleatorio = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9

while numAleatorio != num:
  cont += 1
  num = int(input("Ingrese un número entre el 0 y el 9, puede incluir estos: "))
  if num < 0 or num > 9:
    print("Número fuera de rango, intente nuevamente.")
    continue
  if num < numAleatorio:
    print("El número es mayor.")
  elif num > numAleatorio:
    print("El número es menor.")

print("Felicidades, Has adivinado el número", numAleatorio, "en", cont, "intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

print("Ejercicio 6")

for i in range(100, -1, -2):
  print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

print("Ejercicio 7")

num = int(input("Ingrese un número entero positivo mayor que 0: "))
cont = 0

if num <= 0:
  print("El número debe ser mayor que 0.")  
else:
  for i in range(1, num):
    cont += i

  print ("La cantidad de números comprendidos entre 0 y", num, "es:", cont)


# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("Ejercicio 8")

cantDeNumeros = 100 # este valor puede cambiarse para probar el programa con menos números
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantDeNumeros):
  num = int(input("Ingrese un número entero: "))
  if num % 2 == 0:
    pares += 1
  else:
    impares += 1
  if num >= 0:
    positivos += 1
  elif num < 0:
    negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

print("Ejercicio 9")

cantDeNumeros = 100 # este valor puede cambiarse para probar el programa con menos números
suma = 0
for i in range(cantDeNumeros):
  num = int(input("Ingrese un número entero: "))
  suma += num
media = suma / cantDeNumeros
print("La media de los números ingresados es:", media)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
print("Ejercicio 10")

num = int(input("Ingrese un número para invertir sus dígitos: "))

# Guardar el signo del número en 1 o -1 para luego multiplicarlo por el inverso y asi mantener el signo
signo = 1  
if num < 0:
  signo = -1

# Sacamos el signo para trabajar con el numero positivo
num = abs(num)

inverso = 0

while num > 0: 
    digito = num % 10  #Obtenemos el ultimo digito 
    inverso = inverso * 10 + digito # Lo agregamos al inverso en la posicion de la derecha
    num = num // 10  # Eliminamos el último digito del numero original el cual ya agregamos al inverso
#Esto se repite hasta que se hayan pasado todos los dígitos

inverso *= signo  # Devolvemos el signo al número invertido  (Al multiplicarlo por 1 o -1 no se cambia su valor solo su signo))
print("El número invertido es:", inverso)

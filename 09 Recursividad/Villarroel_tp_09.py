#Ejercicio 1

print ("Ejercicio 1")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
numero = int(input("Ingrese un numero para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")


#Ejercicio 2

print ("\nEjercicio 2")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Ingrese un numero para calcular su posicion en la serie de Fibonacci: "))
resultado = fibonacci(numero)
print(f"El numero en la posicion {numero} de la serie de Fibonacci es: {resultado}")


#Ejercicio 3

print ("\nEjercicio 3")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base} elevado a la {exponente} es igual a: {potencia(base, exponente)}")


#Ejercicio 4

print ("\nEjercicio 4")

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        #(n // 2) Obtengo el cociente
        #(n % 2) Obtengo el residuo
        return decimal_a_binario(n // 2) + str(n % 2) # Concatenacion del bit menos significativo al final 
    
numero = int(input("Ingrese un numero entero positivo en base decimal: "))
binario = decimal_a_binario(numero)

if binario == "": # Manejo del caso cuando el numero es 0
    binario = "0"
print(f"La representacion en binario de {numero} es: {binario}")


#Ejercicio 5

print ("\nEjercicio 5")

def es_palindromo(palabra):
    palabra = palabra.lower().strip()  # Convierto a minúsculas para comparación uniforme y elimino espacios
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] != palabra[-1]:
            return False
        else:
            return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra para verificar si es palindromo: ").lower()
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palindromo.")
else:
    print(f"La palabra '{palabra}' no es un palindromo.")


#Ejercicio 6

print ("\nEjercicio 6")

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10) # Sumo el digito menos significativo y llamo recursivamente con el resto de los digitos

numero = int(input("Ingrese un numero entero positivo para sumar sus digitos: "))
resultado = suma_digitos(numero)
print(f"La suma de los digitos de {numero} es: {resultado}")


#Ejercicio 7

print ("\nEjercicio 7")

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
numero = int(input("Ingrese el numero de bloques en la base de la piramide: "))
resultado = contar_bloques(numero)
print(f"El numero total de bloques en una piramide con base de {numero} bloques es: {resultado}")


#Ejercicio 8

print ("\nEjercicio 8")

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else:
        cuenta = 1 if numero % 10 == digito else 0  # Tomo el último digito y cuento el digito si coincide
        return cuenta + contar_digito(numero // 10, digito) # Llamada recursiva con el resto de los digitos
    
numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito que desea contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El digito {digito} aparece {resultado} veces en el numero {numero}.")


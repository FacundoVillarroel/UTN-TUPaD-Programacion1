# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300 

print("Ejercicio 1:")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario actualizado: {precios_frutas}")


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 ● Manzana = 1700 ● Melón = 2800 

print("\nEjercicio 2:")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Diccionario con precios actualizados: {precios_frutas}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

print("\nEjercicio 3:")

lista_frutas = list(precios_frutas.keys())

print(f"Lista de frutas: {lista_frutas}")


# 4)  Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print("\nEjercicio 4:")
agenda_telefonica = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")

if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es: {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No se encontró el contacto con el nombre {nombre_consulta}.")
    

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

print("\nEjercicio 5:")
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
cantidad_palabras = {}

# Acá recorro el set de palabras únicas y cuento cuántas veces aparece cada una en la lista original
for palabra in palabras_unicas:
    cantidad_palabras[palabra] = palabras.count(palabra) # Uso count para contar las apariciones y lo asigno al diccionario

print(f"Palabras únicas: {palabras_unicas}")
print(f"Cantidad de veces que aparece cada palabra: {cantidad_palabras}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. 

print("\nEjercicio 6:")
alumnos = {}
promedios = {}
for i in range(3):   # hago un bucle para 3 alumnos
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []  # creo una lista vacía para almacenar las notas
    for j in range(1,4): # hago un bucle para 3 notas de cada alumno
        nota = float(input(f"Ingrese la nota {j} de {nombre}: "))
        notas.append(nota) # agrego la nota a la lista
    alumnos[nombre] = tuple(notas) # convierto la lista de notas en una tupla y la asigno al diccionario

# Ahora calculo y muestro el promedio de cada alumno
for alumno in alumnos:
    notas_alumno = alumnos[alumno] # obtengo la tupla de notas del alumno
    suma_notas = sum(notas_alumno) # sumo las notas de la tupla
    promedio = suma_notas / 3 # calculo el promedio sabiendo que son 3 notas

    print(f"El promedio de {alumno} es: {promedio:.2f}") 


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

print("\nEjercicio 7:")

aprobados_parcial_1 = {"Facundo", "María", "Juana", "Pedro", "Lucía"}
aprobados_parcial_2 = {"Facundo", "Ana", "Pedro", "Sofía", "Miguel"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos_parciales = aprobados_parcial_1 & aprobados_parcial_2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

# Estudiantes que aprobaron solo uno de los dos parciales (diferencia simétrica)
solo_un_parcial = aprobados_parcial_1 ^ aprobados_parcial_2
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_un_parcial}")

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_un_parcial = aprobados_parcial_1 | aprobados_parcial_2

print(f"Estudiantes que aprobaron al menos un parcial: {al_menos_un_parcial}")



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

print("\nEjercicio 8:")

stock_productos = {
    "Manzanas": 50,
    "Bananas": 30,
    "Naranjas": 20
}

producto_consulta = input("Ingrese el nombre del producto que desea consultar: ")

# si el producto existe, muestro el stock y pregunto si quiere agregar unidades
if producto_consulta in stock_productos:
    print(f"El stock de {producto_consulta} es: {stock_productos[producto_consulta]}")
    agregar_unidades = int(input(f"¿Cuántas unidades desea agregar al stock de {producto_consulta}? "))
    stock_productos[producto_consulta] += agregar_unidades
    print(f"Nuevo stock de {producto_consulta}: {stock_productos[producto_consulta]}")

# si el producto no existe, pregunto cuántas unidades quiere agregar para crear el producto
else:
    print(f"El producto {producto_consulta} no existe en el stock.")
    nueva_unidades = int(input(f"¿Cuántas unidades desea agregar para crear el producto {producto_consulta}? "))
    stock_productos[producto_consulta] = nueva_unidades
    print(f"Producto {producto_consulta} agregado con un stock de: {stock_productos[producto_consulta]}")
    print(f"Stock actualizado: {stock_productos}")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora.

print("\nEjercicio 9:")

agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "14:00"): "Clases de inglés",
    ("Miércoles", "09:00"): "Parcial de matemáticas",
    ("Jueves", "16:00"): "Llamada con cliente",
    ("Viernes", "12:00"): "Almuerzo con amigos"
}

dia = input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")
hora = input("Ingrese la hora (formato HH:MM): ")
clave_consulta = (dia, hora)

if clave_consulta in agenda:
    print(f"Actividad programada para {dia} a las {hora}: {agenda[clave_consulta]}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora}.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves. 
# • Los países sean los valores. 

print("\nEjercicio 10:")

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Colombia": "Bogotá"}
print(f"Diccionario original: {original}")

paises = original.keys()

invertido = {}

for pais in paises:
    invertido[original[pais]] = pais  # Asigno la capital como clave y el país como valor

print(f"Diccionario invertido: {invertido}")
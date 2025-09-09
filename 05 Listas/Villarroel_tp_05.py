# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja.

print("Ejercicio 1")
notas = [7, 8.5, 6, 9, 5.5, 10, 4, 8, 7.5, 6.5]
print("Lista de notas:", notas)
promedio = sum(notas) / len(notas)
notaMasAlta = max(notas) # max() devuelve el valor máximo de una lista
notaMasBaja = min(notas) # min() devuelve el valor mínimo de una lista
print("Promedio:", promedio)
print("Nota más alta:", notaMasAlta)
print("Nota más baja:", notaMasBaja)


# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print("Ejercicio 2")
productos = []
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)  
print("Lista de productos ordenada alfabéticamente:", sorted(productos))
productoAEliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if productoAEliminar in productos:  # remuevo el producto dentro de un if para evitar error si no existe
    productos.remove(productoAEliminar)
    print("Producto eliminado. Lista actualizada:", productos)
else:
    print("El producto no se encuentra en la lista.")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

print("Ejercicio 3")

import random
numeros = []
for i in range (15) :
  numeros.append(random.randint(1, 100))  # genero un número aleatorio entre 1 y 100 y lo agrego a la lista
print("Lista de números generados:", numeros)
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Números pares:", pares)
print("Números impares:", impares)
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

# 4) Dada una lista con valores repetidos: datos = [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

print("Ejercicio 4")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datosSinRepetidos = []
for num in datos:  # recorro la lista original y voy agregando a datosSinRepetidos solo todavía no está el número.
    if num in datosSinRepetidos:
        continue  # si ya está, no hago nada y sigo con el siguiente número
    else :
        datosSinRepetidos.append(num) # si no está, lo agrego a la nueva lista
print("Lista sin elementos repetidos:", datosSinRepetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

print("Ejercicio 5")
estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]
print("Lista de estudiantes:", estudiantes)
accion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper() # convierto la respuesta a mayúscula para evitar problemas con minúsculas
if accion == "A":   #si la acción es agregar
    nuevoEstudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevoEstudiante)
    print("Estudiante agregado.")
elif accion == "E": #si la acción es eliminar
    estudianteAEliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if estudianteAEliminar in estudiantes:  # remuevo el estudiante dentro de un if para evitar error si no existe
        estudiantes.remove(estudianteAEliminar)
        print("Estudiante eliminado.")
    else:
        print("El estudiante no se encuentra en la lista.")
else: #Si ingreso una acción no válida
    print("Acción no válida.")

#por último, muestro la lista final de estudiantes
print("Lista final de estudiantes:", estudiantes)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero). 

print("Ejercicio 6")
numeros = [10, 20, 30, 40, 50, 60, 70]
print("Lista original:", numeros)
numeros = [numeros[-1]] + numeros[:-1]  # creo una nueva lista con el último elemento seguido de todos los demás excepto el último utilizando slicing
print("Lista rotada:", numeros)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

print("Ejercicio 7")

temperaturas = [
    [20, 25],  # Día 1 
    [17, 28],  # Día 2
    [14, 22],  # Día 3
    [16, 30],  # Día 4
    [18, 27],  # Día 5
    [19, 29],  # Día 6
    [20, 31]   # Día 7
]

sumaMinimas = 0
sumaMaximas = 0
mayorAmplitud = 0
diaMayorAmplitud = 0

for i in range(len(temperaturas)):  # recorro cada día (fila) de la matriz
    minima = temperaturas[i][0] # obtengo la mínima (primera columna)
    maxima = temperaturas[i][1] # obtengo la máxima (segunda columna)
    sumaMinimas += minima  # sumo las mínimas 
    sumaMaximas += maxima  # sumo las máximas
    amplitud = maxima - minima  # calculo la amplitud térmica del día
    if amplitud > mayorAmplitud:  # si la amplitud es mayor que la mayor registrada
        mayorAmplitud = amplitud  # actualizo la mayor amplitud
        diaMayorAmplitud = i   # actualizo el día 

promedioMinimas = sumaMinimas / len(temperaturas)
promedioMaximas = sumaMaximas / len(temperaturas)

dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] 

print("Promedio de temperaturas mínimas:", promedioMinimas)
print("Promedio de temperaturas máximas:", promedioMaximas)
print(f"El día con mayor amplitud termica fue {dias_semana[diaMayorAmplitud]} con una amplitud de {mayorAmplitud} grados.")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

print("Ejercicio 8")

# Matriz de notas: cada fila representa un estudiante y cada columna una materia
notas = [
    [7, 8.5, 6],   # Estudiante 1
    [9, 5.5, 10],  # Estudiante 2
    [4, 8, 7.5],   # Estudiante 3
    [6.5, 7, 8],   # Estudiante 4
    [10, 9, 9.5]   # Estudiante 5
]

# Promedio de cada estudiante}
sumaMaterias = [0, 0, 0]  # lista para sumar las notas de cada materia
for i in range(len(notas)):  # recorro cada estudiante (fila)
    sumaNotas = notas[i][0] + notas[i][1] + notas[i][2]  # sumo las notas de las 3 materias
    promedioEstudiante = sumaNotas / 3   #saco el promedio
    print(f"Promedio del Estudiante {i+1}: {promedioEstudiante}")
    for j in range(len(notas[i])):  # recorro cada materia (columna)
        sumaMaterias[j] += notas[i][j] #sumo la nota de cada materia en su respectiva columna.

# Promedio de cada materia
print("Promedio de cada materia:")
print (f"Materia 1: {sumaMaterias[0] / len(notas)}")
print (f"Materia 2: {sumaMaterias[1] / len(notas)}")
print (f"Materia 3: {sumaMaterias[2] / len(notas)}")



# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

print("Ejercicio 9")

# Inicializo el tablero con guiones
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
] 

turno = 0  # contador de turnos

while turno < 9:  # máximo 9 turnos en una partida de Ta-Te-Ti
    print("Tablero actual:")
    for fila in tablero:  # muestro el tablero
        print(" ".join(fila))  # uno los elementos de la fila con un espacio y lo imprimo
        print() # línea en blanco para separar filas

    jugador = "X" if turno % 2 == 0 else "O" # determino el jugador actual
    print(f"Turno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0, 1, 2): "))
    columna = int(input("Ingrese la columna (0, 1, 2): "))

    if tablero[fila][columna] == "-":  # verifico que la casilla esté vacía
        tablero[fila][columna] = jugador  # coloco la ficha del jugador
        turno += 1 # paso al siguiente turno

    else:  
        print("Casilla ocupada, intente de nuevo.")

    # Muestro el tablero después de la jugada
    print("Tablero después de la jugada:")
    
    for fila in tablero:
        print(" ".join(fila))
        print()

print ("Juego terminado.")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana. 

print("Ejercicio 10")
ventas = [
    [15, 20, 25, 30, 35, 40, 45],  # Producto 1
    [10, 15, 20, 25, 30, 35, 40],  # Producto 2
    [20, 25, 30, 35, 40, 45, 50],  # Producto 3
    [50, 10, 15, 20, 25, 30, 35]    # Producto 4
]

numeroFilas = len(ventas)
numeroColumnas = len(ventas[0])

# Producto más vendido en la semana
productoMasVendido = 0
cantidadProductoMasVendido = 0

# Lista con las ventas totales por día
ventasPorDia = [0,0,0,0,0,0,0]  # lista para sumar las ventas de cada día

for fila in range(len(ventas)):  # recorro cada producto (fila)
    total = sum(ventas[fila])  # sumo las ventas del producto (fila) que esta siendo iterado - (la funcion sum() suma todos los elementos de una lista)
    if total > cantidadProductoMasVendido:  # si el total de ventas del producto por semana es mayor que el mayor registrado
        cantidadProductoMasVendido = total  # actualizo la cantidad del producto más vendido
        productoMasVendido = fila + 1
    print(f"Total vendido del Producto {fila+1}: {total}")
    for columna in range(numeroColumnas):  # recorro cada día (columna)
        ventasPorDia[columna] += ventas[fila][columna]   # sumo las ventas del día en su respectiva columna
        
# al final de recorrer todos los productos, busco el día con mayores ventas totales
diaMayorVentas = 0
cantidadMayorVentas = 0
for i in range(len(ventasPorDia)):  # recorro la lista con las ventas totales por día
    if ventasPorDia[i] > cantidadMayorVentas:
        cantidadMayorVentas = ventasPorDia[i]
        diaMayorVentas = i

print(f"Producto más vendido en la semana: Producto {productoMasVendido} con {cantidadProductoMasVendido} unidades vendidas.")        
print(f"Día con mayores ventas totales: Día {diaMayorVentas + 1} con {cantidadMayorVentas} unidades vendidas.")

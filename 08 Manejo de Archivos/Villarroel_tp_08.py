#Defino una función para leer el archivo y mostrar su contenido
def leer_archivo():
    print("\n Lista de productos: \n")
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            producto = linea.strip().split(",")
            print(f"Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")

#Defino funcion para pedir al usuario un nuevo producto
def pedir_y_agregar_producto():
  print("\nIngrese un nuevo producto: ")
  nombre_producto = input("Ingrese el nombre: ")
  precio_producto = input("Ingrese el precio: ")
  cantidad_producto = input("Ingrese la cantidad: ")

  with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre_producto},{precio_producto},{cantidad_producto}\n")
  #hasta acá cumple con el ejercicio 2 de no modificar todo el archivo completo, pero para cumplir con el ejercicio 6, llamo a la función guardar_lista_productos
  productos = crear_lista_productos()  # Creo la lista de productos actualizada
  guardar_lista_productos(productos)    # Guardo la lista actualizada en el archivo

#Defino una funcion para crear lista de productos desde el archivo 
def crear_lista_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            producto = linea.strip().split(",")
            productos.append({
                "nombre": producto[0],
                "precio": float(producto[1]),
                "cantidad": int(producto[2])
            })
    return productos

#Defino una función para buscar un producto por nombre
def buscar_producto(nombre_buscar):
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            producto = linea.strip().split(",")
            if producto[0].lower() == nombre_buscar.lower(): # Comparo en minúsculas para evitar problemas de mayúsculas/minúsculas
                return {
                    "nombre": producto[0],
                    "precio": float(producto[1]),
                    "cantidad": int(producto[2])
                }
    return None

#Defino función para solicitar al usuario el nombre del producto a buscar
def pedir_y_buscar_producto():
  nombre_a_buscar = input("\nIngrese el nombre del producto a buscar: ")
  producto_encontrado = buscar_producto(nombre_a_buscar)
  if producto_encontrado:
      print(f"Producto encontrado: {producto_encontrado}")
  else:
      print("Error, Producto no encontrado.")

#Defino una función para guardar la lista
def guardar_lista_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

#Menú de opciones para el usuario
while True:
    print("\nMenú de opciones:")
    print("1. Agregar un nuevo producto")
    print("2. Buscar un producto por nombre")
    print("3. Mostrar todos los productos")
    print("4. Mostrar todos los productos en formato de lista de diccionarios")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    match opcion:

          case "1":
              pedir_y_agregar_producto()

          case "2":
              pedir_y_buscar_producto()

          case "3":
              leer_archivo()

          case "4":
              print("\n Lista de productos en formato de lista de diccionarios: \n")
              print(crear_lista_productos())  # Muestro la lista de productos creada (Ejercicio 4)

          case "5":
              print("Saliendo del programa.")
              break 
        
          case _:
              print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
#Ezequiel Margonari 44765363


# Ejercicio n° 1

print("--- EJERCICIO 1 ---")
try:
    a = int(input("Ingresá el dividendo: "))
    b = int(input("Ingresá el divisor: "))
    resultado = a / b
    print("El resultado es: ", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")


# Ejercicio n° 2

print("\n--- EJERCICIO 2 ---")
try:
    num = int(input("Ingresá un número: "))
    texto = str(input("Ingresá un texto: "))
    suma = num + texto
    print(suma)
except TypeError:   
    print("Error: No se puede sumar un número + una cadena")


# Ejercicio n° 3

print("\n--- EJERCICIO 3 ---")
dic = {"nombre": "Ezequiel", "edad": 22}
try:
        coincidencia = input("Ingresá la palabra que querés buscar en el diccionario: ")
        print("Coincidencia encotrada: ", dic[coincidencia])
except KeyError:
    print("Error: Esa palabra no existe en el diciconario.")


# Ejercicio n° 4

print("\n--- EJERCICIO 4 ---")
nombre= input("Ingresá el nombre del archivo que querés abrir: ") 
try:
    with open(nombre, "r") as archivo:
        print("Contenido del archivo:\n", archivo.read())
except FileNotFoundError:
    print("Error: El archivo no existe. Creando un archivo nuevo...")
    with open(nombre, "x") as archivo:
        archivo.write("Este es un archivo nuevo creado automáticamente.\n")


# Ejercicio n° 5

print("\n--- EJEMPLO 5 ---")
try:
    x = int(input("Ingresá el primer número: "))
    y = int(input("Ingresá el segundo número: "))
    print("El resultado es : ", x / y)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Tenés que ingresar números válidos.")
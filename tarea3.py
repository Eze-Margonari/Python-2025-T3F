# EJERCICIO 1
print(" --- EJERCICIO N° 1 --- ")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
mayor = a if a > b else b
print("El mayor es:", mayor)
print("-" * 40)


# EJERCICIO 2

print(" --- EJERCICIO N° 2 --- ")
def buscar_palabra(palabra, *lista):
    return "Encontrada" if palabra in lista else "No encontrada"

lista = input("Ingrese palabras separadas por espacio: ").split()
palabra = input("Ingrese la palabra a buscar: ")
print(buscar_palabra(palabra, *lista))
print("-" * 40)


# EJERCICIO 3

print(" --- EJERCICIO N° 3 --- ")
n = int(input("Ingrese un número: "))
print("Par" if n % 2 == 0 else "Impar")
print("-" * 40)


# EJERCICIO 4

print(" --- EJERCICIO N° 4 --- ")
def promedio(*numeros):
    return sum(numeros) / len(numeros) if len(numeros) > 0 else "Error: no hay números"

numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))
print("Promedio:", promedio(*numeros))
print("-" * 40)

# EJERCICIO 5

print(" --- EJERCICIO N° 5 --- ")
def sumar_dos(a=None, b=None):
    return a + b if a is not None and b is not None else "Error: faltan argumentos"

entrada = input("Ingrese dos números separados por espacio: ").split()

if len(entrada) < 2:
    print("Error: faltan argumentos")
else:
    a, b = map(int, entrada[:2])
    print("Resultado:", sumar_dos(a, b))

print("-" * 40)
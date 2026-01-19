# Las listas en Python son colecciones ordenadas y mutables que permiten almacenar 
# múltiples elementos en una sola variable.

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]
print("Lista original:", mi_lista)

numeros = [10, 20, 30, 40, 50]
numeros_cuadraros = []

for numero in numeros:
    numeros_cuadraros.append(numero ** 2)
    print(f"El cuadrado de {numero} es {numero ** 2}")

# Estructura básica de una lista
#  lista = [ expresion for elemento in iterable ]
# expresion: que hacer con cada elemento
# elemento: cada uno de los elementos del iterable
# iterable: una secuencia (lista, rango, cadena, etc.)

# Filtrar elementos de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print("Números pares:", pares)

# Transformar elementos de una lista
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print("Palabras en mayúsculas:", mayusculas)

# Condicionales
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print("Paridad de los números:", paridad)

# Rangos
potencaias = [2 ** n for n in range(10)]
print("Potencias de 2:", potencaias)

colores = ["rojo", "verde", "azul", "morado"]
objetos = ["carro", "celular", "lapiz", "libro"]

# Ejemplos más avanzados

combinacion = [f"{objeto} {color}" for color in colores for objeto in objetos]
print("Combinación de colores y objetos:", combinacion)

matriz = [[ i * j for j in range(1, 6)] for i in range(1, 6)]
print("Matriz de multiplicación 5x5:", matriz)
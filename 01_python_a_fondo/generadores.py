from typing import Generator

# Un generador es una función que utiliza la palabra clave 'yield' para producir una serie de valores a lo 
# largo del tiempo, en lugar de devolverlos todos a la vez.
def generador_simple() -> Generator:
    print("Inicio del generador")
    yield 1
    print("Después del primer yield")
    yield 2
    print("Después del segundo yield")

for valor in generador_simple():
    print(f"Valor generado: {valor}")

def generador_pares(limite: int) -> Generator:
    for numero in range(limite):
        if numero % 2 == 0:
            yield numero

pares = generador_pares(10)
for par in pares:
    print(f"Número par generado: {par}")

# Ejercicio
def generador_numeros() -> Generator:
    for numero in range(1, 6):
        yield numero

print(list(generador_numeros()))

def generador_letras(palabra) -> Generator:
    for letra in palabra:
        yield letra

print(list(generador_letras("Python")))
for letra in generador_letras("Litzy"):
    print(letra)


generador_pares: Generator = (x for x in range(20) if x % 2 == 0)
print(list(generador_pares))

# Generador infinito
def generador_infinito() -> Generator:
    numero = 1
    while True:
        yield numero
        numero += 1
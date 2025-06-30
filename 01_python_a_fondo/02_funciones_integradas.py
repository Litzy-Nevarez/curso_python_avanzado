# all / any ayuda a saber si todos o algun elemento de un iterable son verdaderos

valores: list[bool] = [True, True, False]
print(all(valores)) # Si todos los valores son verdaderos
print(any(valores)) # Algún valor es verdadero

edad: int = 33
es_adulto: bool = edad >= 18
tiene_liciencia: bool = True
puede_manejar: bool = all([es_adulto, tiene_liciencia])
casi_puede_manejar: bool = any([es_adulto, tiene_liciencia])

# callable: nos dice si algo es llamable
def funcion() -> None:
    pass
print(callable(funcion))
print(callable(34))

# filter(funcion, iterable) ayuda a filtar elementos
def esPar(num) -> bool:
    if num % 2 == 0:
        return True
    else: 
        return False

numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares : list[int] = list(filter(esPar, numeros))
print(pares)
for num in filter(esPar, numeros):
    print(num)

# map(funcion, iterable): retorna un iterable transformado de la funcion
def alCuadrado(num) -> int:
    return num ** 2
numeros: list[int] = [1,2,3,4,5,6]
cuadrados: list[int] = list(map(alCuadrado, numeros))
print(cuadrados)

# sorted(iterable, key=None, reverse=false)
letras: list[str] = ['c', 'a', 'b', 'f', 'e', 'd', 'B']
print(sorted(letras, key=str.lower))

# zip: convina multiples iterables en una tupla
nombres: list[str] = ['Ana', 'Luis', 'Juan']
edades: list[int] = [25, 30, 22]
combinados: list = list(zip(nombres, edades))
print(combinados)
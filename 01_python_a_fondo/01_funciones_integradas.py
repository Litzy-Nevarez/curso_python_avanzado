# print()

# print('Mi', 'nombre', 'es', 'Litzy', sep='\n')
import time

for i in range(3):
    print(f"Cargando {i} ... ", end='', flush=False)
    time.sleep(1)

# isinstance() nos ayuda a verificar el tipo de una variable
x: int = 20
print(isinstance(x, int))
print(isinstance(x, str))

# enumerate: nos retorna un iterador con indices y el valor debe ser alguna secuencia o objeto iterado
frutas: list[str] = ['manzana', 'pera', 'naranja']
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# round(nuemro, ndigits)
numero: float = 12.1234
print(round(numero, 2))
print(round(numero))

# range(stop) / range(start, stop, step=1): nos da un rango de números
for i in range(1, 6):
    print(i)

# slice(stop) / slice(start, stop, step) cortasr listas
numeros: list[int] = [0, 1, 2, 3, 4, 5]
print(numeros.slice(1, 3))

#globals / locals
from pprint import pp
x: int = 42
def ejemplo() -> None:
    y: int = 10
    print("Locales: ", locals())

ejemplo()
#print("Globales: ", globals())
print('Globales: ')
pp(globals())
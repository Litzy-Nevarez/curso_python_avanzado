import random

numero: float = random.random()
print(numero)

numero_entero: int = random.randint(1, 50)
print(numero_entero)

numero_flotante: float = random.uniform(5.5, 8.9)
print(numero_flotante)

colores: list[str] = ['rojo', 'blanco', 'azul', 'verde', 'amarillo']
color_elegido: str = random.choice(colores)
print(f"{color_elegido}")

numeros: list[int] = [1,2,3,4,5,6,7,8,9,10]
seleccionado: list[int] = random.sample(numeros, 3)
print(seleccionado)

# Mover lista a lazar
random.shuffle(numeros)
print(f"{numeros = }")

random.seed(22)
print(random.random())
print(random.random())
print("=============")
random.seed(22)
print(random.random())
print(random.random())
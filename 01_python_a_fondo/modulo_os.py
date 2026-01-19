import os

# Obtener el sistema operativo
print(os.name)

# Ruta actual
print(os.getcwd())

# Cambiar el directorio actual
# os.chdir('ruta/a/directorio')

# Crear directorio
# os.mkdir('nuevo')

# Borrar directorio
# os.rmdir('nuevo')

# Listar contenido
print(os.listdir('.'))

# Comprobar si archivo existe
archivo = 'archivo.txt'
if os.path.exists(archivo):
    print(f"El archivo '{archivo}' existe.")
else:
    print(f"El archivo '{archivo}' no existe.")

# Checar si es archivo
print(os.path.isfile('error.log'))

# Tamaño de archivo
print(os.path.getsize('error.log'))

# Variable de entorno
usuario = os.getenv('USERNAME', 'Desconocido')
print(f"El usuario es: {usuario}")

# Unir rutas
directorio = '/home/user'
archivo = 'documento.txt'

#ruta = os.path.join(directorio, archivo)

# Dividir la ruta en directorio y archivo
ruta = 'C:\\Users\\yulis\\Documents\\curso_python_avanzado\\01_python_a_fondo\\modulo_random.py'
ruta, archivo = os.path.split(ruta)
print(f"Directorio: {ruta}, Archivo: {archivo}")
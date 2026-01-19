'''
    Ejercicio Organizador de archivos

    - Crearemos una función que reciba el directorio(str)
    - Itera en los diferentes archivos
    - Crea un directorio por cada tipo de archivo diferente encontrado
    - Mueve los archivos a sus respectivos directorios
    - Utiliza logging para crear un archivo logs.log donde vaya guardando los logs del proceso
'''
import os
import logging

logging.basicConfig(
    filename='logs.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)


def organizar_archivos(directorio) -> None:
    try:
        os.chdir(directorio)
        logging.info(f"Cambiado al directorio: {directorio}")

        archivos: list[str] = os.listdir()
        logging.info(f"Archivos en el directorio: {archivos}")

        for archivo in archivos:
            if os.path.isfile(archivo):
                extension = archivo.split('.')[-1]

                if not os.path.exists(extension):
                    os.mkdir(extension)
                    logging.info(f"Directorio creado: {extension}")

                destino = os.path.join(extension, archivo)
                os.rename(archivo, destino)
                logging.info(f"Archivo movido: {archivo} a {destino}")

        logging.info("Organización completada.")
                
    except Exception as e:
        logging.error(f"Error al organizar archivos: {e}")
    

directorio = r"C:\Users\yulis\Documents\curso_python_avanzado\directorio_prueba"
organizar_archivos(directorio)
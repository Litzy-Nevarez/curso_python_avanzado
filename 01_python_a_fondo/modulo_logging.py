import logging

logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

'''logging.debug("Este es un mensaje de depuración")
logging.info("Este es un mensaje de info")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error")
logging.critical("Este es un mensaje de critical")'''

def division(a: float, b: float) -> None:
    try:
        resultado: float = a / b
        logging.info(f"Division realizada con exito: {resultado}")
        print(resultado)
    except ZeroDivisionError:
        logging.error("Error: Division entre cero")
        print('Log de error guardado')

division(5, 10)
division(10, 0)
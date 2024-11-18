# Nombre del archivo que deseas abrir
nombre_archivo = 'mi_archivo.txt'  # Asegúrate de que este archivo esté en el mismo directorio que tu script

# Usar la declaración 'with' para abrir el archivo
try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()  # Leer todo el contenido del archivo
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró. Asegúrate de que el nombre del archivo es correcto y que está en el mismo directorio.")
except IOError:
    print(f"Ocurrió un error al intentar leer el archivo '{nombre_archivo}'.")
with open ('leer_readlines.txt', 'r') as archivo:
    lineas = archivo.readlines()  # Lee todas las líneas
    for linea in lineas:
         print (linea.strip())  # Usamos strip() para quitar el EOL al imprimir

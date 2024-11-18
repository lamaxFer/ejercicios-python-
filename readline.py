with open('leer_readline.txt', 'r') as archivo:
    linea1 = archivo.readline()  # Lee la primera línea
    linea2 = archivo.readline()  # Lee la segunda línea
    
    print("Línea 1:", linea1.strip())  # Usar strip() para eliminar saltos de línea
    print("Línea 2:", linea2.strip())  # Usar strip() para eliminar saltos de línea
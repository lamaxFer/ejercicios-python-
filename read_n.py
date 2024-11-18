with open('read_n.txt', 'r') as archivo:
    while True:
        bloque = archivo.read(1024)  # Lee en bloques de 1024 caracteres
        if not bloque:
            break
        print (bloque)

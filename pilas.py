class Pila:
    def __init__(self):
        self.items = []  # Inicializa una lista vacía para almacenar los elementos de la pila

    def is_empty(self):
        return len(self.items) == 0  # Verifica si la pila está vacía

    def push(self, item):
        self.items.append(item)  # Añade un elemento a la parte superior de la pila

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Elimina y devuelve el elemento superior de la pila
        else:
            raise IndexError("No se puede hacer pop de una pila vacía")  
# Manejo de error

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Devuelve el elemento superior sin eliminarlo
        else:
            raise IndexError("No se puede hacer peek de una pila vacía")  
# Manejo de error

    def size(self):
        return len(self.items)  # Devuelve el número de elementos en la pila

# Ejemplo de uso de la pila
mi_pila = Pila()
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(3)

print (mi_pila.pop())  # Salida: 3
print (mi_pila.peek())  # Salida: 2
print (mi_pila.size())  # Salida: 2
print (mi_pila.is_empty())  # Salida: False

mi_pila.pop()  # Elimina 2
mi_pila.pop()  # Elimina 1
print (mi_pila.is_empty())  # Salida: True

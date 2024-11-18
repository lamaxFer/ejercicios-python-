from collections import deque

# Clase para manejar la Cola
class Cola:
    def __init__(self):
        self.items = deque()  # Usamos deque para la cola

    def is_empty(self):
        return len(self.items) == 0  # Comprueba si la cola está vacía

    def enqueue(self, item):
        self.items.append(item)  # Añadir elemento al final de la cola

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Devuelve el primer elemento sin eliminarlo
        else:
            raise IndexError("No se puede hacer peek de una cola vacía")

# Ejemplo de uso
mi_cola = Cola()

# Agregar elementos a la cola usando enqueue
mi_cola.enqueue("Elemento 1")
mi_cola.enqueue("Elemento 2")
mi_cola.enqueue("Elemento 3")

# Ver el primer elemento de la cola usando peek
primer_elemento = mi_cola.peek()
print("Elemento en la parte frontal de la cola (peek):", primer_elemento)  # Salida: Elemento 1
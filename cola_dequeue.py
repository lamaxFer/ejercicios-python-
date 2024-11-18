from collections import deque

# Clase para manejar la Cola
class Cola:
    def __init__(self):
        self.items = deque()  # Usamos deque para la cola

    def is_empty(self):
        return len(self.items) == 0  # Comprueba si la cola está vacía

    def enqueue(self, item):
        self.items.append(item)  # Añadir elemento al final de la cola

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # Elimina y devuelve el primer elemento
        else:
            raise IndexError("No se puede hacer dequeue de una cola vacía")

    def mostrar(self):
        return list(self.items)  # Devuelve la lista de elementos en la cola

# Ejemplo de uso
mi_cola = Cola()

# Agregar elementos a la cola usando enqueue
mi_cola.enqueue("Elemento 1")
mi_cola.enqueue("Elemento 2")
mi_cola.enqueue("Elemento 3")

print("Estado de la cola después de encolar elementos:", mi_cola.mostrar())  # Salida: ['Elemento 1', 'Elemento 2', 'Elemento 3']

# Eliminar un elemento de la cola usando dequeue
elemento_eliminado = mi_cola.dequeue()
print("Elemento eliminado:", elemento_eliminado)  # Salida: Elemento 1
print("Estado de la cola después de hacer dequeue:", mi_cola.mostrar())  # Salida: ['Elemento 2', 'Elemento 3']
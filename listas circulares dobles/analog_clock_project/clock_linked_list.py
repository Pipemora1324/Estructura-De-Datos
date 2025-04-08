# clock_linked_list.py

# Clase que representa cada nodo de hora
class HourNode:
    def __init__(self, hour):
        self.hour = hour  # La hora (1 a 12)
        self.prev = None  # Nodo anterior
        self.next = None  # Nodo siguiente

# Lista circular doble que representa el reloj
class HourClockList:
    def __init__(self):
        self.head = None  # Nodo inicial (hora 1)

    def create_clock(self):
        prev_node = None
        for i in range(1, 13):  # Crear nodos de 1 a 12
            new_node = HourNode(i)
            if self.head is None:
                self.head = new_node
            else:
                prev_node.next = new_node
                new_node.prev = prev_node
            prev_node = new_node

        # Conexiones circulares
        self.head.prev = prev_node
        prev_node.next = self.head

    def print_clock_forward(self):
        # Prueba: imprimir de 1 a 12
        current = self.head
        for _ in range(12):
            print(f"Hora: {current.hour}")
            current = current.next

    def print_clock_backward(self):
        # Prueba: imprimir de 12 a 1
        current = self.head.prev
        for _ in range(12):
            print(f"Hora: {current.hour}")
            current = current.prev

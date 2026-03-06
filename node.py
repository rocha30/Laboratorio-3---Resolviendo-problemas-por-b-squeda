class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        """
        state: nombre del nodo (string)
        parent: nodo padre (para reconstruir el camino)
        g: costo acumulado desde el inicio
        h: valor heurístico
        """
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        """
        Necesario para que Python pueda comparar nodos
        en la Priority Queue (heapq).
        """
        return self.f < other.f

    def __repr__(self):
        return f"Node({self.state}, g={self.g}, h={self.h}, f={self.f})"
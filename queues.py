import heapq


# ==============================
# FIFO Queue (BFS)
# ==============================

class FIFOQueue:
    def __init__(self):
        self.queue = []

    def EMPTY(self):
        return len(self.queue) == 0

    def TOP(self):
        return self.queue[0] if not self.EMPTY() else None

    def POP(self):
        return self.queue.pop(0) if not self.EMPTY() else None

    def ADD(self, element):
        self.queue.append(element)
        return self.queue


# ==============================
# LIFO Queue (DFS)
# ==============================

class LIFOQueue:
    def __init__(self):
        self.stack = []

    def EMPTY(self):
        return len(self.stack) == 0

    def TOP(self):
        return self.stack[-1] if not self.EMPTY() else None

    def POP(self):
        return self.stack.pop() if not self.EMPTY() else None

    def ADD(self, element):
        self.stack.append(element)
        return self.stack


# ==============================
# Priority Queue (UCS, Greedy, A*)
# ==============================

class PriorityQueue:
    def __init__(self, priority_function):
        """
        priority_function: función que recibe un nodo
        y retorna el valor por el cual se ordenará.
        """
        self.heap = []
        self.priority_function = priority_function
        self.counter = 0  # evita problemas cuando prioridades son iguales

    def EMPTY(self):
        return len(self.heap) == 0

    def TOP(self):
        return self.heap[0][2] if not self.EMPTY() else None

    def POP(self):
        if not self.EMPTY():
            return heapq.heappop(self.heap)[2]
        return None

    def ADD(self, element):
        priority = self.priority_function(element)
        heapq.heappush(self.heap, (priority, self.counter, element))
        self.counter += 1
        return self.heap
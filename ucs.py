from node import Node
from queues import PriorityQueue


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def ucs(graph, start, goal):
    # PriorityQueue usando g(n)
    frontier = PriorityQueue(lambda node: node.g)

    start_node = Node(state=start, g=0)
    frontier.ADD(start_node)

    explored = {}

    while not frontier.EMPTY():
        current_node = frontier.POP()

        # Si llegamos al objetivo
        if current_node.state == goal:
            return reconstruct_path(current_node), current_node.g

        # Si ya lo exploramos con menor costo, lo ignoramos
        if current_node.state in explored and explored[current_node.state] <= current_node.g:
            continue

        explored[current_node.state] = current_node.g

        # Expandir vecinos
        if current_node.state in graph:
            for neighbor, cost in graph[current_node.state].items():
                new_g = current_node.g + cost
                child = Node(state=neighbor, parent=current_node, g=new_g)
                frontier.ADD(child)

    return None, float("inf")
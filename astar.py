from node import Node
from queues import PriorityQueue


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def astar(graph, heuristic, start, goal):
    # PriorityQueue usando f(n) = g + h
    frontier = PriorityQueue(lambda node: node.f)

    start_node = Node(state=start, g=0, h=heuristic[start])
    frontier.ADD(start_node)

    explored = {}

    while not frontier.EMPTY():
        current_node = frontier.POP()

        # Si llegamos al objetivo
        if current_node.state == goal:
            return reconstruct_path(current_node), current_node.g

        # Si ya lo exploramos con menor o igual costo, lo ignoramos
        if current_node.state in explored and explored[current_node.state] <= current_node.g:
            continue

        explored[current_node.state] = current_node.g

        # Expandir vecinos
        if current_node.state in graph:
            for neighbor, cost in graph[current_node.state].items():
                new_g = current_node.g + cost
                new_h = heuristic.get(neighbor, 0)

                child = Node(
                    state=neighbor,
                    parent=current_node,
                    g=new_g,
                    h=new_h
                )

                frontier.ADD(child)

    return None, float("inf")
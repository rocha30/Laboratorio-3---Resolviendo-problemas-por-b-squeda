from node import Node
from queues import PriorityQueue


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def greedy(graph, heuristic, start, goal):
    # PriorityQueue usando SOLO h(n)
    frontier = PriorityQueue(lambda node: node.h)

    start_node = Node(state=start, g=0, h=heuristic[start])
    frontier.ADD(start_node)

    explored = set()

    while not frontier.EMPTY():
        current_node = frontier.POP()

        if current_node.state == goal:
            return reconstruct_path(current_node), current_node.g

        if current_node.state in explored:
            continue

        explored.add(current_node.state)

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
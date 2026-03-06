from node import Node
from queues import FIFOQueue


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def bfs(graph, start, goal):
    frontier = FIFOQueue()

    start_node = Node(state=start)
    frontier.ADD(start_node)

    explored = set()

    while not frontier.EMPTY():
        current_node = frontier.POP()

        if current_node.state == goal:
            return reconstruct_path(current_node)

        if current_node.state in explored:
            continue

        explored.add(current_node.state)

        if current_node.state in graph:
            for neighbor in graph[current_node.state]:
                child = Node(
                    state=neighbor,
                    parent=current_node
                )
                frontier.ADD(child)

    return None
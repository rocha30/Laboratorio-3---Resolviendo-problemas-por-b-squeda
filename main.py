from graph_loader import load_graph, load_heuristic
from ucs import ucs
from astar import astar
from greedy import greedy
from bfs import bfs
from dfs import dfs 

def main():
    # Cargar archivos
    graph = load_graph("funcion_de_costo.xlsx")
    heuristic = load_heuristic("heuristica.xlsx")

    start = "Warm-up activities"
    goal = "Stretching"

    print("===== UNIFORM COST SEARCH =====")
    path_ucs, cost_ucs = ucs(graph, start, goal)
    print("Path:", path_ucs)
    print("Cost:", cost_ucs)

    print("\n===== A* SEARCH =====")
    path_astar, cost_astar = astar(graph, heuristic, start, goal)
    print("Path:", path_astar)
    print("Cost:", cost_astar)
    
    print("\n===== GREEDY BEST-FIRST SEARCH =====")
    path_greedy, cost_greedy = greedy(graph, heuristic, start, goal)
    print("Path:", path_greedy)
    print("Cost:", cost_greedy)
    
    
    print("\n===== BREADTH-FIRST SEARCH =====")
    path_bfs = bfs(graph, start, goal)
    print("Path:", path_bfs)

    print("\n===== DEPTH-FIRST SEARCH =====")
    path_dfs = dfs(graph, start, goal)
    print("Path:", path_dfs)


if __name__ == "__main__":
    main()
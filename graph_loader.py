import pandas as pd


cost_file = "funcion_de_costo.xlsx"
heuristic_file = "heuristic.xlsx"

def load_graph(cost_file):
    """
    Lee el archivo de costos y construye
    un diccionario tipo:
    
    {
        "NodoA": {"NodoB": costo, "NodoC": costo},
        ...
    }
    """
    df = pd.read_excel(cost_file)

    graph = {}

    for _, row in df.iterrows():
        origin = row["Origen"]
        destination = row["Destino"]
        cost = row["Cost"]

        if origin not in graph:
            graph[origin] = {}

        graph[origin][destination] = cost


    return graph


def load_heuristic(heuristic_file):
    """
    Lee el archivo de heurística y construye
    un diccionario tipo:
    
    {
        "NodoA": valor_heurístico,
        ...
    }
    """
    df = pd.read_excel(heuristic_file)

    heuristic = {}

    for _, row in df.iterrows():
        node = row["Activity"]
        h_value = row["Recovery time after burning 300cal (minutes)"]

        heuristic[node] = h_value

    return heuristic
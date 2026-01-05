from copy import deepcopy

def adjacency_matrix(graph, nodes):
    adj_matrix = [[float("inf") for node in nodes] for node in nodes]
    node_d = {node: i for i, node in enumerate(nodes)}

    for u, edges in graph.items():
        for v, weight in edges:
            v1 = node_d[v]
            u1 = node_d[u]
            adj_matrix[u1][v1] = weight
    return adj_matrix


def floyd_warshall(edges: list[list]):
    edges_copy = deepcopy(edges)
    n = len(edges_copy)

    predecessor = [[None if edges_copy[u][v] == float("inf")  else u for u in range(n)] for v in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if edges_copy[i][k] != float("inf") and edges_copy[k][j] != float("inf"):
                    if edges_copy[i][k] + edges_copy[k][j] < edges_copy[i][j]:
                        edges_copy[i][j] = edges_copy[i][k] + edges_copy[k][j]
                        predecessor[i][j] = predecessor[i][k]

    for i in range(n):
        if edges_copy[i][i] == 1:
            return -1

    return edges_copy, predecessor
LALALA = [[inf, 12, inf, 8, 14, inf], [12, inf, 3, inf, 15, 5], [inf, 3, inf, 5, 2, 5], [8, inf, 5, inf, inf, inf], [14, 15, 2, inf, inf, 4], [inf, 5, 5, inf, 4, inf]]

graph = {
    "A": [("B", 12), ("D", 8), ("E", 14)],
    "B": [("A", 12), ("C", 3), ("E", 15), ("F", 5)],
    "C": [("B", 3), ("D", 5), ("E", 2), ("F", 5)],
    "D": [("A", 8), ("C", 5)],
    "E": [("A", 14), ("B", 15), ("C", 2), ("F", 4)],
    "F": [("B", 5), ("C", 5), ("E", 4)]
}

print(adjacency_matrix(graph, ["A", "B", "C", "D", "E", "F"]))

def bellmanford(edges, nodes, start):
    predecessor = {v: None for v in nodes}
    cost = {v: float("inf") for v in nodes}
    cost[start] = 0

    for i in range(len(nodes) - 1):
        flag = False
        for u, v, weight in edges:
            if cost[u] != float('inf') and cost[u] + weight < cost[v]:
                cost[v] = cost[u] + weight
                predecessor[v] = u
                flag = True
        if not flag:
            break

    for u, v, weight in edges:
        if cost[u] != float("inf") and cost[u] + weight < cost[v]:
            return -1

    return cost, predecessor


edges =[
    ["A", "B", 6],
    ["A", "C", 4],
    ["A", "D", 5],
    ["B", "E", -1],
    ["C", "B", -2],
    ["C", "E", 3],
    ["D", "C", -2],
    ["D", "F", -1],
    ["E", "F", 3]
]

print(bellmanford(edges, ["A", "B", "C", "D", "E", "F"], "A"))
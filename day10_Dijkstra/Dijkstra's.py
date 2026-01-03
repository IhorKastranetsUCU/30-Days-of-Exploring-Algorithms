import heapq

def dijkstra(graph: dict, nodes: list, start):
    path_len = {v: float("inf") for v in nodes}
    path_len[start] = 0
    parents = {v: None for v in nodes}
    minHeap = [[0, start]]

    while minHeap:
        w1, v1 = heapq.heappop(minHeap)
        if w1 > path_len[v1]:
            continue

        for v2, w2 in graph[v1]:
            weight = w2 + w1
            if weight < path_len[v2]:
                path_len[v2] = weight
                parents[v2] = v1
                heapq.heappush(minHeap, (weight, v2))
    return  path_len, parents


graph = {
    "A": [("B", 12), ("D", 8), ("E", 14)],
    "B": [("A", 12), ("C", 3), ("E", 15), ("F", 5)],
    "C": [("B", 3), ("D", 5), ("E", 2), ("F", 5)],
    "D": [("A", 8), ("C", 5)],
    "E": [("A", 14), ("B", 15), ("C", 2), ("F", 4)],
    "F": [("B", 5), ("C", 5), ("E", 4)]
}

print(dijkstra(graph,   ["A", "B", "C", "D", "E", "F"], "A"))
def bellman_ford(graph : list , n : int , v ):
    dist = [float("inf")]*n
    prev = [-1] * n

    def update(dist : list ,prev : list , el):
        par , to , w = el[0] , el[1] ,el[2]
        tmp = dist[to]

        if dist[par] == float("inf"):
            return

        dist[to] = min(dist[to] , dist[par] + w )

        if tmp != dist[to]:
            prev[to] = par


    dist[v] = 0
    for i in range(n-1):
        for el in graph:
            update(dist , prev , el)

    return dist , prev


if __name__ == "__main__":
    V = 5
    S = 0

    edges = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3]
    ]

    print(bellman_ford(edges , V , S))

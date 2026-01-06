class Graph:
    def __init__(self, graph):
        self.graph = graph

    def adjacency_matrix(self):
        nodes = self.graph.keys()
        adj_matrix = [[0 for node in nodes] for node in nodes]
        node_d = {node: i for i, node in enumerate(nodes)}

        for u, edges in self.graph.items():
            for v, weight in edges:
                v1 = node_d[v]
                u1 = node_d[u]
                adj_matrix[u1][v1] = weight
        return adj_matrix


    def BFS(self, s, t):
        parent = [-1] * len(self.graph)
        visited = {s}
        queue = [s]

        while queue:
            u = queue.pop(0)
            for i, val in enumerate(self.graph[u]):
                if i in visited or val <= 0:
                    continue
                queue.append(i)
                visited.add(i)
                parent[i] = u
                if i == t:
                    return True, parent
        return False, parent


    def FordFulkerson(self, source, target):
        max_flow = 0

        while True:
            res, parent = self.BFS(source, target)
            if not res:
                break

            path_flow = float("inf")
            t = target
            while t != source:
                path_flow = min(path_flow, self.graph[parent[t]][t])
                t = parent[t]

            max_flow += path_flow
            v = target
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

graph = {
    "S": [('A', 12), ('B', 7), ('C', 5)],
    "A": [('D', 15), ('E', 8)],
    "B": [('D', 10), ('T', 9)],
    "C": [('B', 14), ('E', 6)],
    "D": [('T', 13)],
    "E": [('C', 11), ('T', 4)],
    "T": []
}

g = Graph(graph)
g.graph = g.adjacency_matrix()

max_flow = g.FordFulkerson(0, 4)
print(max_flow)
class DisjointSet():
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        v1, v2 = self.find(v1), self.find(v2)

        if v1 == v2:
            return False

        if self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        elif self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1

        return True

def kruskal(graph):
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
    edges.sort(key = lambda edge: (edge[2], edge[0], edge[1]))

    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)

    tree = []
    for v1, v2, weight in edges:
        v1 = disjoint_set.find(v1)
        v2 = disjoint_set.find(v2)
        if v1 != v2:
            tree.append((v1, v2, weight))
            disjoint_set.union(v1, v2)

    return tree

graph = {
    "A": [("B", 12), ("D", 8), ("E", 14)],
    "B": [("A", 12), ("C", 3), ("E", 15), ("G", 5)],
    "C": [("B", 3), ("D", 5), ("E", 2), ("G", 5)],
    "D": [("A", 8), ("C", 5)],
    "E": [("A", 14), ("B", 15), ("C", 2), ("G", 4)],
    "G": [("B", 5), ("C", 5), ("E", 4)]
}

print(kruskal(graph))
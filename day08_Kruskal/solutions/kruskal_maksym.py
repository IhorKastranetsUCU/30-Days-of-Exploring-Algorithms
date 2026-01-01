class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parents[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            elif self.rank[root_a] > self.rank[root_b]:
                self.parents[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parents[root_b] = root_a
                self.rank[root_a] += 1
                self.size[root_a] += self.size[root_b]
            return True
        return False


    def __str__(self):
        return str(self.parents)

def kruskal(num_vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) of a graph.
    """
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSet(num_vertices)
    mst_edges = []
    total_cost = 0

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges, total_cost

if __name__ == "__main__":
    edges = [
        [0, 1, 10],
        [0, 2, 6],
        [0, 3, 5],
        [1, 3, 15],
        [2, 3, 4]
    ]
    num_vertices = 4

    mst, cost = kruskal(num_vertices, edges)
    print(mst , cost)
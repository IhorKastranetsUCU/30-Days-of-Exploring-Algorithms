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


def minCostConnectPoints(self, points: list[list[int]]) -> int:
    def kruskal(num_vertices, edges):
        edges.sort(key=lambda x: x[2])

        dsu = DisjointSet(num_vertices)
        mst_edges = []
        total_cost = 0

        edges_count = 0

        for u, v, weight in edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, weight))
                total_cost += weight
                edges_count += 1

                if edges_count == num_vertices - 1:
                    break

        return total_cost

    n = len(points)
    all_edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            all_edges.append([i, j, dist])

    return kruskal(n, all_edges)

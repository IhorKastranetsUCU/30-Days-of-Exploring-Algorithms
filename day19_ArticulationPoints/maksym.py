import sys
sys.setrecursionlimit(200000)

class CutVerticesFind:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.used = [0] * self.n
        self.tin = [0] * self.n
        self.low = [0] * self.n
        self.timer = 0
        self.cut_vertices = set()

    def add_edge(self, u, v, idx):
        self.graph[u].append((v, idx))
        self.graph[v].append((u, idx))

    def dfs(self, v, p=-1, edge_idx=-1):
        self.used[v] = 1
        self.tin[v] = self.low[v] = self.timer
        self.timer += 1
        children = 0  # Лічильник дітей для кореня

        for to, idx in self.graph[v]:
            if idx == edge_idx:
                continue

            if self.used[to]:
                # Зворотне ребро
                self.low[v] = min(self.low[v], self.tin[to])
            else:
                # Пряме ребро дерева
                children += 1
                self.dfs(to, v, idx)
                self.low[v] = min(self.low[v], self.low[to])

                if p != -1 and self.low[to] >= self.tin[v]:
                    self.cut_vertices.add(v)


        if p == -1 and children > 1:
            self.cut_vertices.add(v)

    def find_cut_vertices(self):
        self.timer = 0
        self.cut_vertices = set()
        self.used = [0] * self.n

        for i in range(self.n):
            if not self.used[i]:
                self.dfs(i, -1, -1)

        return sorted(list(self.cut_vertices))

if __name__ == "__main__":
    bf = CutVerticesFind(7)

    # Твій тестовий граф:
    # 0-1-2 (цикл), 2-3 (міст), 3-4-5 (цикл), 5-6 (хвіст)
    edges = [
        [0, 1], [1, 2], [2, 0],  # Left Triangle
        [2, 3],                  # The Bridge
        [3, 4], [4, 5], [5, 3],  # Right Triangle
        [5, 6]                   # The Leaf "Tail"
    ]

    for i, el in enumerate(edges):
        bf.add_edge(el[0], el[1], i)

    print(f"Points: {bf.find_cut_vertices()}")

class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.id = 0
        self.scc_count = 0

        self.ids = [-1] * n
        self.low = [0] * n
        self.on_stack = [False] * n
        self.stack = []



        self.bridges = []
        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_sccs(self):
        for i in range(self.n):
            if self.ids[i] == -1:
                self.dfs(i)
        return self.sccs

    def dfs(self, at):
        self.stack.append(at)
        self.on_stack[at] = True
        self.ids[at] = self.low[at] = self.id
        self.id += 1

        for to in self.graph[at]:
            if self.ids[to] == -1:
                self.dfs(to)
                self.low[at] = min(self.low[at], self.low[to])

            elif self.on_stack[to]:
                self.low[at] = min(self.low[at], self.ids[to])

        if self.ids[at] == self.low[at]:
            current_scc = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                current_scc.append(node)
                if node == at:
                    break

            self.sccs.append(current_scc)
            self.scc_count += 1

    def find_bridges(self):
        if self.ids[0] == -1:
            self.dfs(0,)
        return self.bridges



if __name__ == "__main__":
    n = 8
    t = TarjanSCC(n)

    edges = [
        (0, 1), (1, 2), (2, 0),
        (2, 3),
        (3, 4),
        (4, 5), (5, 6), (6, 4),
        (6, 7)
    ]

    for u, v in edges:
        t.add_edge(u, v)

    t.find_sccs()

    print("Component IDs per node:", t.sccs)

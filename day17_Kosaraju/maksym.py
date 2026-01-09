class Kosaraju:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.traversal = [[] for _ in range(n)]
        self.used = [0]*self.n
        self.topsort = []

    def add_edge(self, u , v):
        self.graph[u].append(v)
        self.traversal[v].append(u)

    def topsort_dfs(self, v ):
        if self.used[v] == 1:
            return

        self.used[v] = 1

        for to in self.graph[v]:
            self.topsort_dfs(to)

        self.topsort.append(v)


    def scc_dfs(self, v , comp):
        if self.used[v] != 0:
            return

        self.used[v] = comp

        for to in self.traversal[v]:
            self.scc_dfs(to , comp)

    def scc(self):
        for i in range(self.n):
            self.topsort_dfs(i)

        self.used = [0]*self.n

        self.topsort.reverse()

        comp = 1
        for v in self.topsort:
            if self.used[v] == 0:
                self.scc_dfs(v, comp)
                comp+=1


    def bridges(self):
        bridges = []
        for v in range(self.n):
            for to in self.graph[v]:
                if self.used[v]!=self.used[to]:
                    bridges.append((v,to))
        return bridges


if __name__ == "__main__":
    # Number of nodes: 8 (0 to 7)
    # Expected SCCs:
    # 1. [0, 1, 2]
    # 2. [3]
    # 3. [4, 5, 6, 7]

    edges = [
        # --- SCC 1 (The Root Component) ---
        (0, 1),
        (1, 2),
        (2, 0),    # Closes cycle 0-1-2

        # --- Bridge from SCC 1 to SCC 2 ---
        (1, 3),

        # --- SCC 2 (Single Node Component) ---
        # Node 3 has a self-loop or just sits there.
        # Let's make it flow into the next component.
        (3, 4),

        # --- SCC 3 (The Sink Component - Complex Cycle) ---
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),    # Closes big outer cycle 4-5-6-7
        (5, 7)     # Internal shortcut (cross-edge) inside the SCC
    ]

    # If your Kosaraju implementation expects a class method:
    # for u, v in edges:
    #     g.add_edge(u, v)

    k = Kosaraju(8)
    for e in edges:
        k.add_edge(e[0], e[1])

    k.scc()
    print(k.used)
    print(k.bridges())

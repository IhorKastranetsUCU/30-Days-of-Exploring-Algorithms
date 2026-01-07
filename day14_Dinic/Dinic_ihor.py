class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = [0] * n
        self.ptr = [0] * n


    def add_edge(self, u, v, cap):
        forward = Edge(v, cap, len(self.graph[v]))
        backward = Edge(u, 0, len(self.graph[u]))

        self.graph[u].append(forward)
        self.graph[v].append(backward)


    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0

        queue = [s]

        while queue:
            u = queue.pop(0)
            for edge in self.graph[u]:
                # ще не відвідано + є залишкова ємність
                if self.level[edge.to] == -1 and edge.cap > 0:
                    self.level[edge.to] = self.level[u] + 1
                    queue.append(edge.to)

        return self.level[t] != -1


    def dfs(self, u, t, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        while self.ptr[u] < len(self.graph[u]):
            edge = self.graph[u][self.ptr[u]]
            if (
                self.level[edge.to] == self.level[u] + 1
                and edge.cap > 0
            ):
                flow = self.dfs(
                    edge.to,
                    t,
                    min(pushed, edge.cap)
                )
                if flow > 0:
                    edge.cap -= flow
                    self.graph[edge.to][edge.rev].cap += flow
                    return flow
            self.ptr[u] += 1
        return 0


    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed

        return flow


g = Dinic(5)

g.add_edge(0, 1, 12)
g.add_edge(0, 2, 27)
g.add_edge(0, 3, 5)
g.add_edge(1, 4, 15)
g.add_edge(1, 5, 8)
g.add_edge(2, 4,  10)
g.add_edge(2, 6, 9)
g.add_edge(3, 2, 14)
g.add_edge(3, 5, 6)
g.add_edge(4, 6, 13)
g.add_edge(5, 6, 20)



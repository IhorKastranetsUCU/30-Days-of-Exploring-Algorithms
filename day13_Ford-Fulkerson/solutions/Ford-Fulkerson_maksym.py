class FordFulkerson:
    def __init__(self , n):
        self.size = n
        self.graph = [[] for _ in range(n)]
        self.visited = [0] * n

    def add_edge(self, u , v ,cap):
        forward = [ v , cap , 0 , len(self.graph[v]) ] # v, cap, current_flow, rev_idx
        backward = [ u , 0 , 0 , len(self.graph[u]) ]

        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def dfs(self , u  , t , flow ):
        if u == t:
            return flow

        self.visited[u] = 1
        for i in range(len(self.graph[u])):
            v , cap , cur_flow , idx = self.graph[u][i]

            if not self.visited[v] and cap - cur_flow > 0:
                neck = self.dfs( v, t , min(flow ,  cap - cur_flow ))

                if neck > 0:
                    self.graph[u][i][2] += neck
                    self.graph[v][idx][2] -= neck
                    return neck

        return 0

    def max_flow(self, s, t):
        max_flow = 0

        while True:

            self.visited = [0] * self.size
            path = self.dfs(s, t, float('inf'))

            if path == 0:
                break

            max_flow +=path

        return max_flow



if __name__ == "__main__":

    V = 6
    source = 0
    sink = 5


    edges = [
        [0, 1, 16],
        [0, 2, 13], # Source -> Node 2 (Cap 13)
        [1, 2, 10], # Node 1 -> Node 2 (Cap 10)
        [1, 3, 12], # Node 1 -> Node 3 (Cap 12)
        [2, 4, 14], # Node 2 -> Node 4 (Cap 14)
        [3, 2, 9],  # Node 3 -> Node 2 (Cap 9)
        [3, 5, 20], # Node 3 -> Sink (Cap 20)
        [4, 3, 7],  # Node 4 -> Node 3 (Cap 7)
        [4, 5, 4]   # Node 4 -> Sink (Cap 4)
    ]
    res = FordFulkerson(V)
    for u,v,cap in edges:
        res.add_edge(u,v,cap)

    print(res.max_flow(source , sink))


    # ==========================================
    # Expected Output
    # ==========================================
    # The Maximum Flow should be: 23
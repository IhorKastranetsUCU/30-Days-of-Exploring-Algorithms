import sys
sys.setrecursionlimit(200000)

class BridgeFind:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.used = [0] * self.n
        self.tin = [0] * self.n
        self.tmin = [0] * self.n
        self.timer = 0
        self.bridges = []

    def add_edge(self , u , v , idx ):
        self.graph[u].append((v,idx))
        self.graph[v].append((u,idx))

    def dfs(self , v , par , edge ):
        self.used[v] = 1
        self.tin[v] = self.tmin[v] = self.timer
        self.timer += 1

        for to , e in self.graph[v]:
            if e == edge:
                continue

            if self.used[to] == 0:
                self.dfs(to ,v , e)

                self.tmin[v] = min(self.tmin[v], self.tmin[to])

                if self.tmin[to] > self.tin[v]:
                    self.bridges.append(e)
            else:
                self.tmin[v] = min(self.tmin[v], self.tin[to])

    def find_bridges(self):
        for i in range(self.n):
            if self.used[i] == 0:
                self.dfs(i, -1, -1)

        return sorted(self.bridges)

if __name__ == "__main__":
    print("Running Bridge Test...")

    # Initialize graph with 6 nodes
    bf = BridgeFind(6)

    edges = [
        # (u, v, edge_index)

        # 1. A Triangle Cycle (0-1-2) -> No bridges here
        (0, 1, 101),
        (1, 2, 102),
        (2, 0, 103),

        # 2. A Bridge connecting the triangle to the rest
        (0, 3, 200),  # <--- EXPECTED BRIDGE

        # 3. Parallel Edges between 3 and 4 -> No bridges here!
        # Because if you cut edge 301, edge 302 still connects them.
        (3, 4, 301),
        (3, 4, 302),

        # 4. A Dead-end Bridge connected to node 4
        (4, 5, 400)   # <--- EXPECTED BRIDGE
    ]

    # Add edges to the graph
    for u, v, idx in edges:
        bf.add_edge(u, v, idx)
        print(f"Added Edge {idx}: {u} -- {v}")

    # Run Algorithm
    result = bf.find_bridges()

    print("-" * 30)
    print(f"Found Bridges: {result}")

    # Verification
    expected = [200, 400]
    if result == expected:
        print("✅ SUCCESS: Correct bridges identified.")
    else:
        print(f"❌ FAILURE: Expected {expected}, got {result}")
        print("Hint: If you see [301, 302], your code fails to handle parallel edges.")

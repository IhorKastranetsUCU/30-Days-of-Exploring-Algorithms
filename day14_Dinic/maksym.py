from typing import List

class Dinic:
    def __init__(self , n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u , v , cap):
        forward  = [ v , cap  , len(self.graph[v]) ]

        backward  = [ u , 0  , len(self.graph[u]) - 1  ]

        self.graph[v].append(backward)
        self.graph[u].append(forward)

    def bfs(self, s , t):
        self.level= [-1] * (self.n)
        self.level[s] = 0

        q = Queue([s])

        while q:
            u = q.pop_front()
            for v, cap , rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0 :
                    self.level[v] = self.level[u] + 1
                    q.append(v)

        return self.level[t] >= 0

    def dfs(self, u, t ,flow , ptr):
        if u == t or flow == 0:
            return flow

        for i in range(ptr[u] , len(self.graph[u]) ):
            ptr[u] = i

            v, cap , rev = self.graph[u][i]

            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t , min(flow , cap) ,ptr)

                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed

        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s,t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s,t, float('inf') ,ptr)
                if pushed == 0:
                    break
                max_f +=pushed

        return max_f

class Queue:
    def __init__(self, array=None):
        if array is None:
            self.q = []
        else:
            self.q = list(array)
        self.index = 0

    def append(self, el):
        self.q.append(el)

    def pop_front(self):
        if self.index >= len(self.q):
            return None

        val = self.q[self.index]
        self.index += 1
        return val

    def __len__(self):
        return len(self.q) - self.index

    def __bool__(self):
        return self.index < len(self.q)

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        row = len(seats)
        cols = len(seats[0])

        s = row * cols
        t = row * cols + 1

        mx = Dinic(t+1)


        total = 0

        directions = [
            (0 , -1) , ( 0 , 1),
            (-1, -1) , (-1 , 1),
            (1,-1) , (1 , 1)
        ]

        for r in range(row):
            for c in range(cols):
                if seats[r][c] == "#":
                    continue

                total+=1
                u = r*cols + c

                if c%2 == 0:
                    mx.add_edge(s , u , 1)
                    for dr , dc in directions:
                        nr , nc = r + dr , c+ dc
                        if 0 <= nr < row and 0 <= nc < cols:
                            if seats[nr][nc] == '.':
                                v = nr * cols + nc
                                mx.add_edge(u , v , float('inf') )
                else:
                    mx.add_edge( u , t , 1)

        res = mx.max_flow(s,t)

        return total - res

if __name__ == "__main__":

    print(Solution.maxStudents(Solution , [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]))


    d = Dinic(6)
    # Edges from previous examples
    d.add_edge(0, 1, 16)
    d.add_edge(0, 2, 13)
    d.add_edge(1, 2, 10)
    d.add_edge(1, 3, 12)
    d.add_edge(2, 1, 4)
    d.add_edge(2, 4, 14)
    d.add_edge(3, 2, 9)
    d.add_edge(3, 5, 20)
    d.add_edge(4, 3, 7)
    d.add_edge(4, 5, 4)

    print(d.max_flow(0, 5)) # Output: 23

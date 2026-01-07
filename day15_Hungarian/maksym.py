import sys

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, cap):
        forward = [v, cap, 0, len(self.graph[v])]
        backward = [u, 0, 0, len(self.graph[u])]
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, flow, rev in self.graph[u]:
                if cap - flow > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, pushed, ptr):
        if pushed == 0 or u == t:
            return pushed

        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, flow, rev = self.graph[u][i]

            if self.level[v] != self.level[u] + 1 or cap - flow == 0:
                continue

            tr = self.dfs(v, t, min(pushed, cap - flow), ptr)
            if tr == 0:
                continue


            self.graph[u][i][2] += tr
            self.graph[v][rev][2] -= tr
            return tr

        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow

class OptimalAssignmentHungarian:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.matrix = [row[:] for row in matrix]
        self.added_edges = [[False] * self.n for _ in range(self.n)]
        self.dinic = None

    def reduction(self):
        for i in range(self.n):
            r_min = min(self.matrix[i])
            for j in range(self.n):
                self.matrix[i][j] -= r_min

        for j in range(self.n):
            c_min = min(self.matrix[i][j] for i in range(self.n))
            for i in range(self.n):
                self.matrix[i][j] -= c_min

    def get_vertex_cover(self):
        row_covered = [False] * self.n
        col_covered = [False] * self.n


        for i in range(self.n):
            if self.dinic.level[i + 1] == -1:
                row_covered[i] = True

        for j in range(self.n):
            if self.dinic.level[self.n + 1 + j] != -1:
                col_covered[j] = True

        return row_covered, col_covered

    def shift_zeros(self, row_covered, col_covered):
        k = float('inf')
        for i in range(self.n):
            if not row_covered[i]:
                for j in range(self.n):
                    if not col_covered[j]:
                        if self.matrix[i][j] < k:
                            k = self.matrix[i][j]

        if k == float('inf') or k == 0: return

        for i in range(self.n):
            for j in range(self.n):
                if row_covered[i]:
                    self.matrix[i][j] += k
                if not col_covered[j]:
                    self.matrix[i][j] -= k

    def solve(self):
        self.reduction()

        s, t = 0, 2 * self.n + 1
        self.dinic = Dinic(2 * self.n + 2)

        for i in range(self.n):
            self.dinic.add_edge(s, i + 1, 1)
        for j in range(self.n):
            self.dinic.add_edge(self.n + 1 + j, t, 1)

        total_matching = 0

        while True:
            for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j] == 0 and not self.added_edges[i][j]:
                        self.dinic.add_edge(i + 1, self.n + 1 + j, 1)
                        self.added_edges[i][j] = True

            delta = self.dinic.max_flow(s, t)
            total_matching += delta

            if total_matching == self.n:
                break

            row_cov, col_cov = self.get_vertex_cover()
            self.shift_zeros(row_cov, col_cov)


        result_pairs = []
        for u in range(1, self.n + 1):
            for v, cap, flow, rev in self.dinic.graph[u]:
                if flow == 1 and v > self.n and v != t:
                    result_pairs.append((u - 1, v - (self.n + 1)))
        return result_pairs



import numpy as np
from scipy.optimize import linear_sum_assignment
import time

def solve_assignment_fast(matrix):
    cost_matrix = np.array(matrix)

    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    total_cost = cost_matrix[row_ind, col_ind].sum()

    return row_ind, col_ind, total_cost

if __name__ == "__main__":
    import time
    import random

    def generate_matrix(n, min_val=1, max_val=100):
        return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]

    matrix = generate_matrix(10000)

    t1 = time.time()
    correct_res = solve_assignment_fast(matrix)
    t2 = time.time()

    print(t2-t1)

    solver = OptimalAssignmentHungarian(matrix)

    t1 = time.time()
    res = solver.solve()
    t2 = time.time()

    print(t2-t1)

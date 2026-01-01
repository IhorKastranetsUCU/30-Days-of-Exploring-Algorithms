import time
import random
import matplotlib.pyplot as plt
import math


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

def heapify(arr : list , v : int , n : int) -> list:
    left_child = 2*v+1
    right_child = 2*v+2
    largest = v

    if left_child < n and arr[left_child] < arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] < arr[largest]:
        largest = right_child

    if largest!=v:
        arr[v] , arr[largest] = arr[largest] , arr[v]

        heapify(arr , largest , n)

def heap(arr : list) -> list :
    n = len(arr)
    for i in range( n//2 -1 , -1 , -1):
        heapify(arr, i , n)
    return arr

def insert_in_heap(arr: list, v: int):
    arr.append(v)
    current = len(arr) - 1

    while current > 0:
        parent = (current - 1) // 2
        if arr[current] < arr[parent]:
            arr[current], arr[parent] = arr[parent], arr[current]
            current = parent
        else:
            break

def heap_pop(arr : list):
    arr[-1], arr[0] = arr[0], arr[-1]
    res = arr.pop()
    heapify(arr, 0, len(arr))
    return res


def prims_adjencylist(graph : dict, v : int):
    res_arr = []
    dsu = DisjointSet(len(graph))
    min_heap = heap([])
    while len(res_arr) < len(graph)-1:
        for neighbor , value in graph[v]:
            insert_in_heap(min_heap , (value , v , neighbor) )

        while len(min_heap) > 0:
            to_edge  = heap_pop(min_heap)

            if dsu.find(to_edge[1]) != dsu.find(to_edge[2]):
                dsu.union(to_edge[1] , to_edge[2])
                res_arr.append( ( to_edge[1] ,to_edge[2] ,to_edge[0] ) )
                v = to_edge[2]
                break

    mst_val = sum([el[2] for el in res_arr ])

    return res_arr , mst_val

def my_algorithm(num_vertices, input_data):

    prims_adjencylist(input_data , 0)

    time.sleep(0.0001 * num_vertices)
    return 0

# --- 2. INPUT GENERATOR ---
def generate_dense_graph(n):
    """
    Generates a dense graph (E approx V^2) in Edge List format.
    Good for testing Prim's vs Kruskal's performance limits.
    """
    edges = []
    for i in range(n - 1):
        w = random.randint(1, 100)
        edges.append([i, i+1, w])

    limit = min(n * (n - 1) // 2, n * 100)
    seen = set((i, i+1) for i in range(n - 1))

    while len(edges) < limit:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (u, v) not in seen and (v, u) not in seen:
            w = random.randint(1, 100)
            edges.append([u, v, w])
            seen.add((u, v))

    return edges

def convert_to_adj(n, edges):
    """Helper if your algo needs Adjacency List instead of Edges"""
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj

def run_benchmark():

    test_sizes = [i*100 for i in range(1,35)] # Adjust based on speed
    times = []
    prob_time = []

    print(f"{'Vertices':<10} | {'Edges':<10} | {'Time (Seconds)':<15}")
    print("-" * 40)

    for n in test_sizes:

        edges = generate_dense_graph(n)
        input_data = convert_to_adj(n,edges)

        start_time = time.time()

        my_algorithm(n, input_data)

        end_time = time.time()
        duration = end_time - start_time
        times.append(duration)
        prob_time.append(  ( n*n) )

        print(f"{n:<10} | {len(edges):<10} | {duration:.6f}")

    return test_sizes, times

if __name__ == "__main__":
    start_time = time.time()

    counter = 0
    for i in range(int(1.5*1e7)):
        counter+=1

    end_time = time.time()
    duration = end_time - start_time

    sizes, times = run_benchmark()

    print(duration)
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, times, marker='o', linestyle='-', color='b')
        plt.plot(sizes, [ int(i*i/duration) for i in sizes], marker='x', linestyle='-', color='r')
        plt.plot(sizes, [int(i*math.log(i,2)/duration) for i in sizes], marker='v', linestyle='-', color='g')
        plt.title("Algorithm Time Complexity Analysis")
        plt.xlabel("Number of Vertices (N)")
        plt.ylabel("Execution Time (Seconds)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        print("\n(Matplotlib not found, skipping graph. Install it to see the plot.)")

# if __name__ == "__main__":


#     # in case of matrix input
#     # from collections import defaultdict
#     # edges = [
#     #     [0, 1, 10],
#     #     [0, 2, 6],
#     #     [0, 3, 5],
#     #     [1, 3, 15],
#     #     [2, 3, 4]
#     # ]

#     # adj_list = defaultdict(list)
#     # for u, v, weight in edges:
#     #     adj_list[u].append((v, weight))
#     #     adj_list[v].append((u, weight))
#     # print(dict(adj_list))

#     num_vertices = 10
#     adj_list = {
#         0: [(1, 4), (7, 8), (5, 9)],
#         1: [(0, 4), (2, 8), (7, 11), (5, 12)],
#         2: [(1, 8), (3, 7), (8, 2), (5, 4), (9, 7)],
#         3: [(2, 7), (4, 9), (5, 14), (8, 5)],
#         4: [(3, 9), (5, 10), (9, 3)],
#         5: [(2, 4), (3, 14), (4, 10), (6, 2), (0, 9), (1, 12), (9, 8)],
#         6: [(5, 2), (7, 1), (8, 6)],
#         7: [(0, 8), (1, 11), (6, 1), (8, 7)],
#         8: [(2, 2), (6, 6), (7, 7), (3, 5)],
#         9: [(4, 3), (5, 8), (2, 7)]
#     }
#     ans = [(0, 1, 4), (0, 7, 8), (7, 6, 1), \
#                 (6, 5, 2), (5, 2, 4), (2, 8, 2), (8, 3, 5), (2, 9, 7), (9, 4, 3)]

#     mst , price = prims_adjencylist(adj_list , 0)
#     print(mst, price)

#     assert set(ans) == set(mst)

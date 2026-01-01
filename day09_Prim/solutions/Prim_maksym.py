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


        if len(min_heap) == 0:
            break


        while len(min_heap) > 0:
            to_edge  = heap_pop(min_heap)

            if dsu.find(to_edge[1]) != dsu.find(to_edge[2]):
                dsu.union(to_edge[1] , to_edge[2])
                res_arr.append( ( to_edge[1] ,to_edge[2] ,to_edge[0] ) )
                v = to_edge[2]
                break

    mst_val = sum([el[2] for el in res_arr ])

    return res_arr , mst_val

if __name__ == "__main__":


    # in case of matrix input
    # from collections import defaultdict
    # edges = [
    #     [0, 1, 10],
    #     [0, 2, 6],
    #     [0, 3, 5],
    #     [1, 3, 15],
    #     [2, 3, 4]
    # ]

    # adj_list = defaultdict(list)
    # for u, v, weight in edges:
    #     adj_list[u].append((v, weight))
    #     adj_list[v].append((u, weight))
    # print(dict(adj_list))

    num_vertices = 10
    adj_list = {
        0: [(1, 4), (7, 8), (5, 9)],
        1: [(0, 4), (2, 8), (7, 11), (5, 12)],
        2: [(1, 8), (3, 7), (8, 2), (5, 4), (9, 7)],
        3: [(2, 7), (4, 9), (5, 14), (8, 5)],
        4: [(3, 9), (5, 10), (9, 3)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2), (0, 9), (1, 12), (9, 8)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7), (3, 5)],
        9: [(4, 3), (5, 8), (2, 7)]
    }
    ans = [(0, 1, 4), (0, 7, 8), (7, 6, 1), \
                (6, 5, 2), (5, 2, 4), (2, 8, 2), (8, 3, 5), (2, 9, 7), (9, 4, 3)]

    mst , price = prims_adjencylist(adj_list , 0)
    print(mst, price)

    assert set(ans) == set(mst)
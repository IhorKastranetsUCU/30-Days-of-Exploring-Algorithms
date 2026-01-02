from typing import Callable, List

class Heap:

    def __init__(self , comparator : Callable = (lambda x,y : x < y) ):
        self.heap = []
        self.comp = comparator

    def __str__(self):
        return str(self.heap)

    def push_down(self , v):
        n = len(self.heap)
        while True:
            left = 2*v+1
            right = 2*v+2
            most = v

            if left < n and self.comp( self.heap[left], self.heap[most] ):
                most = left
            if right < n and self.comp( self.heap[right], self.heap[most] ):
                most = right

            if most != v:
                self.heap[v] , self.heap[most] = self.heap[most] , self.heap[v]
                v = most
            else:
                break

    def push_up(self , v):
        while v > 0:
            parents = (v-1) //2
            if self.comp(self.heap[v] , self.heap[parents]):
                self.heap[v] , self.heap[parents] = self.heap[parents] , self.heap[v]
                v = parents
            else:
                break

    def insert(self , el ):
        self.heap.append(el)
        self.push_up(len(self.heap)-1)

    def pop(self):
        if not self.heap:
            return None

        self.heap[0] , self.heap[-1] = self.heap[-1] , self.heap[0]
        pop_element = self.heap.pop()

        if self.heap:
            self.push_down(0)

        return pop_element

    def build_heap_from_array(self, array : list):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.push_down(i)

    def size(self):
        return len(self.heap)



def Dijkstra(graph : dict , v):

    dheap = Heap(lambda x,y : x < y)
    dheap.insert( ( 0, v ) )

    visited = {}

    while dheap.size() > 0:
        weight, to = dheap.pop()

        if to in visited:
            continue

        visited[to] = weight

        if to in graph:
            for sus , sus_w in graph[to]:
                if sus not in visited:
                    new_distance = weight + sus_w
                    dheap.insert((new_distance, sus))

    return visited

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)

        for edge in times:
            u = edge[0]
            v = edge[1]

            weight = edge[2]
            val_forward = (v, weight)
            graph[u].append(val_forward)

            if v not in graph:
                graph[v] = []

        result = Dijkstra(graph, k)
        ans = max(result.values())
        if len(result)!=n:
            return -1

        return ans


if __name__ == "__main__":
    n = 5

    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
    }


    start_node = 0
    print(Dijkstra(graph , start_node))

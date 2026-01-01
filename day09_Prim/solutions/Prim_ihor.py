class MinHeap:
    def __init__(self):
        self.array = []

    def insert(self, el):
        self.array.append(el)
        self.push_up(len(self.array) - 1)

    def pop(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop()

        min_el = self.array[0]
        self.array[0] = self.array.pop()
        self.push_down(0)
        return min_el

    def push_down(self, i):
        n = len(self.array)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.array[left] < self.array[smallest]:
                smallest = left
            if right < n and self.array[right] < self.array[smallest]:
                smallest = right

            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def push_up(self, i):
        parent_index = (i - 1) // 2
        while i > 0 and self.array[i] < self.array[parent_index]:
            self.swap(i, parent_index)
            i = parent_index
            parent_index = (i - 1) // 2

    def __str__(self):
        return " ".join([str(i) for i in self.array])


def prim(graph, node):
    visited = set([node])
    mst = []

    heap = MinHeap()

    for to_node, weight in graph[node]:
        heap.insert((weight, node, to_node))

    while heap.array:
        weight, from_node, to_node = heap.pop()
        if to_node in visited:
            continue

        visited.add(to_node)
        mst.append((from_node, to_node, weight))

        for next_node, w in graph[to_node]:
            if next_node not in visited:
                heap.insert((w, to_node, next_node))

    return mst

graph = {
    "A": [("B", 12), ("D", 8), ("E", 14)],
    "B": [("A", 12), ("C", 3), ("E", 15), ("G", 5)],
    "C": [("B", 3), ("D", 5), ("E", 2), ("G", 5)],
    "D": [("A", 8), ("C", 5)],
    "E": [("A", 14), ("B", 15), ("C", 2), ("G", 4)],
    "G": [("B", 5), ("C", 5), ("E", 4)]
}
print(prim(graph, "A"))
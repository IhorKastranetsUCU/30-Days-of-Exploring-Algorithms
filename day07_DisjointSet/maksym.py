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


    def __str__(self):
        return str(self.parents)


if __name__ == "__main__":
    dis_set = DisjointSet(6)
    print(dis_set.find(1))
    print(dis_set)
    dis_set.union(0,1)
    print(dis_set)
    dis_set.union(0,2)
    print(dis_set)

    dis_set.union(3,4)
    print(dis_set)
    dis_set.union(3,5)
    print(dis_set)
    dis_set.union(3,2)
    print(dis_set.find(2) == dis_set.find(5))
    print(dis_set)

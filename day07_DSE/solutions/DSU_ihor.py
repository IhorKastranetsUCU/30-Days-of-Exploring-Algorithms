# Version 1 O(n)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parent[y] = x


# Version 2 O(log(n))
class UnionFind2:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x > y:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]



# Version 3 O(a(x)) find(optimization)

class UnionFind3:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            if self.parent[x] > self.parent[y]:
                self.parent[y] = x
                self.rank[x] += 1
            else:
                self.parent[x] = y
                self.rank[y] += 1

    def __str__(self):
        return str(self.parent)




var = UnionFind3(5)
print(var.union(4, 1))

array = (6, 12, 4, 9, 13, 2)
dsu = UnionFind3(len(array))
print(dsu)

dsu.union(1, 3)
print(f"1, 3: {dsu}")

dsu.union(2, 3)
print(f"2, 3: {dsu}")

dsu.union(4, 0)
print(f"3, 0: {dsu}")


dsu.union(4, 2)
print(f"3, 4: {dsu}")

dsu.union(3, 5)
print(f"3, 5: {dsu}")

dsu.union(1, 2)
print(f"3, 5: {dsu}")
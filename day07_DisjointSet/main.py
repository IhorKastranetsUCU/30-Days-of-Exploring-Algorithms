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

def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    unique_nums = list(set(nums))

    dsu = DisjointSet(len(unique_nums))

    val_to_index = {num: i for i, num in enumerate(unique_nums)}

    for num in unique_nums:
        if (num - 1) in val_to_index:
            curr_idx = val_to_index[num]
            prev_idx = val_to_index[num - 1]
            dsu.union(curr_idx, prev_idx)

    return max(dsu.size)

def equationsPossible(equations: list[str]) -> bool:
    dsu = DisjointSet(27)

    for equ in equations:
        if equ[1] == "=":
            dsu.union( ord(equ[0])-ord("a") ,ord(equ[-1])-ord("a") )

    for equ in equations:
        if equ[1] == "!":
            if dsu.find ( ord(equ[0])-ord("a") )  == dsu.find( ord(equ[-1])-ord("a") ):
                return False
    return True





if __name__ == "__main__":
    #nums = [0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999]
    #print(longestConsecutive(nums))
    equations = ["b==a","a==b"]
    print(equationsPossible(equations))

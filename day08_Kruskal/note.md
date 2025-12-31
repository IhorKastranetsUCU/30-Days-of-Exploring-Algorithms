# Day 8
___
## Overall
Today is the 8th day of the challenge, and I feel tired due to poor sleep over the last three days.  
My physical energy is less than 30%, and furthermore, my mental state is worse than at the beginning 
of the challenge. I am overthinking about failing, and I plan to discuss it with some people.  

It annoys me that writing notes takes more time than writing code. I am also disappointed by 
how few likes I get on my LinkedIn posts, even though I try my best to write good descriptions
and create interesting animations using `manim`.  

I feel that someday I might burn out. But I have a few reasons to continue:  
- **Firstly**, one reason is the expectation of a reward. I will order a PowerMeter on the day 
- I finish the 30th day. Also, registration for EURO2026 starts in just a week, and I don’t want to miss it.  
- **Secondly**, I feel a sense of accomplishment when I grasp something I didn’t understand before.  
- **Thirdly**, I notice that my writing in English improves: my sentence structures 
now look more natural, and I make far fewer syntax mistakes than before.  
- **Fourthly**, I write code more confidently.  

In conclusion, I did my best in the first week, and I will try to continue improving myself.
___

## Disjoint Set Union
Kruskal's Algorithm uses Disjoint Set data structure. So before I started learning this algorithm
I decided to solve 2 problems on LeetCode on this topic. I implemented this data structure by myself
and solved the problem without hints because the idea was clear, but with using AI to fix bugs.

Problems that I solved:
- 1061. Lexicographically Smallest Equivalent String
- 547. Number of Provinces

___

## Kruskal's algorithm
It has very simple idea, we sort the edges by weights and makes union from chepest cost to the most
expensive avoiding loops.
___

## LeetCode problems
### 1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
```python 
class DisjointSet():
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        v1, v2 = self.find(v1), self.find(v2)

        if v1 == v2:
            return False

        if self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        elif self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1

        return True

class Solution:
    def kruskal(self, graph):
        edges = []
        for u, neighbors in graph.items():
            for v, w in neighbors:
                edges.append((u, v, w))

        edges.sort(key=lambda e: e[2])
        ds = DisjointSet(graph.keys())

        mst = []
        for u, v, w in edges:
            if ds.union(u, v):
                mst.append((u, v, w))
        return mst

    def minCostConnectPoints(self, points):
        graph = {}
        n = len(points)

        for i in range(n):
            graph[i] = []
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((j, dist))

        mst = self.kruskal(graph)
        return sum(w for _, _, w in mst)
```
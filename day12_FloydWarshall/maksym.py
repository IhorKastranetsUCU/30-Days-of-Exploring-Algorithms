from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        end = max(nums)

        eratosfen = [(1 , [1])] * int(end+10)


        for i in range(2 ,end+1):
            for j in range(i,end+1, i):
                eratosfen[j] = (eratosfen[j][0]+1 ,eratosfen[j][1]+[i] )

        #print(eratosfen)
        res = 0
        for el in nums:
            if eratosfen[el][0] == 4:
                res+=sum(eratosfen[el][1])

        return res


def Floyd_Warshall(graph: list[list], n: int):
    INF = float('inf')

    for k in range(n):
        for i in range(n):
            if graph[i][k] == INF:
                continue

            dist_ik = graph[i][k]

            for j in range(n):
                new_dist = dist_ik + graph[k][j]
                if graph[i][j] > new_dist:
                    graph[i][j] = new_dist

    return graph

def matrix_convert(edges: list, n: int):
    INF = float('inf')
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for u, v_node, w in edges:
        graph[u][v_node] = w

    return graph


if __name__ == "__main__":
    n = 4

    INF = float('inf')

    edges = [
        [0, 1, 5],
        [0, 3, 10],
        [1, 2, 3],
        [2, 3, 1]
    ]

    graph_matrix = [
        [0,   5,   INF, 10],
        [INF, 0,   3,   INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]
    ]

    expected_matrix = [
        [0,   5,   8,   9],   # 0 can reach 1(5), 2(5+3=8), 3(5+3+1=9)
        [INF, 0,   3,   4],   # 1 can reach 2(3), 3(3+1=4)
        [INF, INF, 0,   1],   # 2 can reach 3(1)
        [INF, INF, INF, 0]    # 3 cannot reach anyone
    ]


    assert Floyd_Warshall(matrix_convert(edges , n), n )== expected_matrix

    #print(Solution.sumFourDivisors(Solution, [21,21]))

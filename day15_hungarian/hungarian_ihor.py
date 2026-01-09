import numpy as np

class Solution:
    def maxCompatibilitySum(self, students, mentors):
        students = np.array(students)
        mentors = np.array(mentors)
        n = students.shape[0]

        cost = np.array([[np.sum(students[i] == mentors[j]) for j in range(n)] for i in range(n)], dtype=int)

        cost = -cost

        return int(self.hungarian(cost))

    def hungarian(self, cost):
        n = cost.shape[0]
        u = np.zeros(n+1, dtype=int)
        v = np.zeros(n+1, dtype=int)
        p = np.zeros(n+1, dtype=int)
        way = np.zeros(n+1, dtype=int)

        for i in range(1, n+1):
            p[0] = i
            minv = np.full(n+1, np.inf)
            used = np.zeros(n+1, dtype=bool)
            j0 = 0
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = np.inf
                j1 = -1
                for j in range(1, n+1):
                    if not used[j]:
                        cur = cost[i0-1, j-1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(n+1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while j0 != 0:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1

        ans = 0
        for j in range(1, n+1):
            i = p[j]
            ans += -cost[i-1, j-1]
        return int(ans)
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sub = []
        for i, row in enumerate(matrix):
            c = 0
            for j , el in enumerate ( row ) :
                if el < 0 :
                    c+=1
                matrix[i][j] = abs(matrix[i][j])
            sub.append(c % 2)
        num = sum(sub) % 2
        m_num = float('inf')
        print(sub)
        if num:
            for row in matrix:
                m_num = min(m_num , min( row ) )
        else:
            m_num = 0

        res = 0
        for row in matrix:
            res+=sum(row)
        print(res)
        return res-m_num*2

if __name__ == "__main__":
    print(Solution.maxMatrixSum(Solution,[[1,2,3],[-1,-2,-3],[1,2,3]]) )

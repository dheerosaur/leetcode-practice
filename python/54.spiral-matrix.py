"""
Spiral
"""
from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        u, l, r, d = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        while l < r and u < d:
            result.extend([matrix[u][i] for i in range(l, r)])
            result.extend([matrix[i][r] for i in range(u, d)])
            result.extend([matrix[d][i] for i in range(r, l, -1)])
            result.extend([matrix[i][l] for i in range(d, u, -1)])
            l, u = l + 1, u + 1
            r, d = r - 1, d - 1
        if l == r:
            result.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            result.extend([matrix[u][i] for i in range(l, r + 1)])
        return result


def test():
    sol = Solution()
    cases = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ],
        [],
        [[]],
        [[1]],
        [[1, 2, 3, 4]],
        [[1], [2], [3], [4]],
    ]
    for case in cases:
        print(sol.spiralOrder(case))
        # assert sol.spiralOrder() == sol.spiralOrder_2()


if __name__ == '__main__':
    test()

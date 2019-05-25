"""
Diagonal traversal
"""
from typing import List
import collections


class Solution:
    def findDiagonalOrder_i(self, matrix: [List[List[int]]]) -> List[int]:
        entries = [(i + j, (j, i)[(i ^ j) & 1], val)
                   for i, row in enumerate(matrix)
                   for j, val in enumerate(row)]
        return [e[2] for e in sorted(entries)]

    def findDiagonalOrder(self, matrix: [List[List[int]]]) -> List[int]:
        def sorter(xy):
            x, y = xy
            return (x + y, x if (x + y) % 2 else y)

        m, n = len(matrix), len(matrix[0])
        indices = sorted(((i, j) for i in range(m) for j in range(n)),
                         key=sorter)
        return [matrix[i][j] for i, j in indices]

    def findDiagonalOrder_dd(self, matrix: [List[List[int]]]) -> List[int]:
        result = []
        dd = collections.defaultdict(list)
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                dd[i + j].append(val)
        for k in sorted(dd.keys()):
            diag = dd[k] if k % 2 else reversed(dd[k])
            result.extend(diag)
        return result


def test():
    sol = Solution()
    cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
    for case in cases:
        print(sol.findDiagonalOrder(case))


if __name__ == '__main__':
    test()

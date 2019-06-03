from typing import List
import collections


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ctr = collections.Counter()
        for row in matrix:
            ctr[tuple(row)] += 1
            ctr[tuple((1 - x) for x in row)] += 1
        return max(ctr.values())


def test():
    sol = Solution()
    cases = [
        [[0, 1], [1, 1]],
        [[0, 0, 0], [0, 0, 1], [1, 1, 0]],
    ]
    for case in cases:
        print(sol.maxEqualRowsAfterFlips(case))


if __name__ == '__main__':
    test()

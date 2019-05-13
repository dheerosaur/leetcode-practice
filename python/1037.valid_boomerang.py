"""
A boomerang is a set of 3 points that are all distinct and not in a straight
line.

Given a list of three points in the plane, return whether these points are a
boomerang.

"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p, q, r = (x1, y1), (x2, y2), (x3, y3) = points
        if p in (q, r):
            return False
        return (y2 - y1) * (x3 - x1) != (x2 - x1) * (y3 - y1)


def test():
    sol = Solution()
    cases = [
        [[1, 1], [2, 3], [3, 2]],
        [[1, 1], [2, 2], [3, 3]],
        [[1, 1], [1, 2], [1, 3]],
        [[0, 1], [0, 1], [2, 1]],
    ]
    for case in cases:
        print(sol.isBoomerang(case))
        # assert sol.isBoomerang() == sol.isBoomerang_2()


if __name__ == '__main__':
    test()

# Given an array A of integers and integer K, return the maximum S such that
# there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying
# this equation, return -1.
from itertools import combinations
from typing import List


class Solution:
    def twoSumLessThanK_n2(self, A: List[int], K: int) -> int:
        gen = (x + y for x, y in combinations(A, 2) if x + y < K)
        return max([-1, *gen])

    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        left, right = 0, len(A) - 1
        closest = -1
        while left < right:
            total = A[left] + A[right]
            if closest < total < K:
                closest = total
            if total < K:
                left += 1
            else:
                right -= 1
        return closest


def test():
    sol = Solution()
    cases = [
        ([34, 23, 1, 24, 75, 33, 54, 8], 60),
        ([10, 20, 30], 15),
        ([10, 20, 30], 40),
    ]
    for case in cases:
        print(sol.twoSumLessThanK(*case))
        print(sol.twoSumLessThanK_n2(*case))


if __name__ == "__main__":
    test()

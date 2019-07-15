#
# @lc app=leetcode id=46 lang=python3
# [algorithms] - Medium
#
# [46] Permutations
# https://leetcode.com/problems/permutations/description/
#
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
# Approach:
# Let list be a1, a2, a3, ... an.
# Permutations are [
#  [a1, perm(a2, a3, ,,, an)]
#  [perm(a2, a3, ,,, an), a1]
# We use recursion to do this for smaller and smaller lists
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return output


def test():
    sol = Solution()
    cases = [
        [1, 2, 3],
    ]
    for case in cases:
        print(sol.permute(case))


if __name__ == '__main__':
    test()

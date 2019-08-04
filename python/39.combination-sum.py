#
# @lc app=leetcode id=39 lang=python3
# [algorithms] - Medium
#
# [39] Combination Sum
# https://leetcode.com/problems/combination-sum/description/
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(target, chosen, i=0):
            if target == 0:
                result.append(chosen)
                return
            for j, c in enumerate(candidates[i:]):
                if target - c >= 0:
                    helper(target - c, chosen + [c], i + j)

        helper(target, [])
        return result


def test():
    sol = Solution()
    cases = [
        # (candidates, target)
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
    ]
    for case in cases:
        print(sol.combinationSum(*case))


if __name__ == "__main__":
    test()

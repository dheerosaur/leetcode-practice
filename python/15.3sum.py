"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List
from collections import defaultdict


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        S = sorted(nums)
        result = set()
        for i in range(0, n - 1):
            start = i + 1
            end = n - 1
            while start < end:
                total = S[i] + S[start] + S[end]
                if total == 0:
                    result.add((S[i], S[start], S[end]))
                    while start < end and S[start] == S[start + 1]:
                        start += 1
                    while start < end and S[start] == S[start + 1]:
                        end -= 1
                    start, end = start + 1, end - 1
                elif total > 0:
                    end = end - 1
                else:
                    start = start + 1
        return [list(x) for x in result]

    def threeSum_n2(self, nums: List[int]) -> List[List[int]]:
        num_set = defaultdict(set)
        result = set()
        for i, num in enumerate(nums):
            num_set[num].add(i)

        for j, num in enumerate(nums):
            for k in range(j + 1, len(nums)):
                required = 0 - nums[j] - nums[k]
                for ind in num_set[required]:
                    if ind not in (j, k):
                        tup = tuple(sorted([required, nums[j], nums[k]]))
                        result.add(tup)
        return [list(x) for x in result]

    def threeSum_bf(self, nums: List[int]) -> List[List[int]]:
        "Brute force O(n^3)"
        result = set()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tup = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(tup)
        return [list(x) for x in result]


def test():
    sol = Solution()
    cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 0, 0, 1, 1, -1],
        range(-1, 2),
        range(10),
    ]
    for case in cases:
        print(sol.threeSum(case))
        print(sol.threeSum_n2(case))
        print(sol.threeSum_bf(case))


if __name__ == '__main__':
    test()

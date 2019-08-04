#
# @lc app=leetcode id=763 lang=python3
# [algorithms] - Medium
#
# [763] Partition Labels
# https://leetcode.com/problems/partition-labels/description/
#
#
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
#
#
#
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
#
#
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans, max_pos = [], {}
        for i, c in enumerate(S):
            max_pos[c] = i

        last, local_max = 0, 0
        for i, c in enumerate(S):
            if i > local_max:
                ans.append(local_max + 1 - last)
                last = local_max + 1
            local_max = max(local_max, max_pos[c])
        ans.append(local_max + 1 - last)
        return ans


def test():
    sol = Solution()
    cases = [
        # cases
        "ababcbacadefegdehijhklij",
        "ababcbacadepfegdehijhklij",
    ]
    for case in cases:
        print(sol.partitionLabels(case))


if __name__ == "__main__":
    test()

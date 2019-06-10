#
# @lc app=leetcode id=402 lang=python3
# [algorithms] - Medium
#
# [402] Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
#
#
# Note:
#
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
import re


class Solution:
    def removeKdigitsQ(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        K, q = k, []
        for i in num:
            while q and q[-1] > i and k > 0:
                q.pop()
                k -= 1
            q.append(i)
        return ''.join(q[:len(num) - K]).lstrip('0') or '0'

    def removeKdigits(self, num: str, k: int) -> str:
        sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]'
                         '|7[0-6]|8[0-7]|9[0-8]|.$').sub  # noqa
        for _ in range(k):
            num = sub(lambda m: m.group()[1:], num, 1)
        return num.lstrip('0') or '0'


def test():
    sol = Solution()
    cases = [
        ("1432219", 3),
        ("1173", 2),
        ("10200", 1),
        ("1000200", 2),
        ("10", 2),
        ("1431209", 4),
        ("77506259332", 6),
        ("77506259332", 5),
        ("123", 2),
    ]
    for case in cases:
        s1 = sol.removeKdigits(*case)
        s2 = sol.removeKdigitsQ(*case)
        assert s1 == s2


if __name__ == '__main__':
    test()

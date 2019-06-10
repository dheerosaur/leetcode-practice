#
# @lc app=leetcode id=28 lang=python3
# [algorithms] - Easy
#
# [28] Implement strStr()
# https://leetcode.com/problems/implement-strstr/description/
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#


class Solution:
    def strStr_basic(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            for j, c in enumerate(needle):
                if haystack[i + j] != c:
                    break
            else:
                return i
        return -1 if needle else ''

    def strStrPy(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m):
            for j in range(n):
                if i + j == m:
                    return -1
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


def test():
    sol = Solution()
    cases = [
        ("mississippi", "ppi"),
        ("mississippi", "issipi"),
    ]
    for case in cases:
        print(sol.strStr(*case))


if __name__ == '__main__':
    test()

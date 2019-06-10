#
# @lc app=leetcode id=616 lang=python3
# [algorithms] - Medium
#
# [616] Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/description/
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them.
#
# Example 1:
#
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#
# Example 2:
#
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
# Note:
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Find ranges of strings
        ranges = []
        for pattern in words:
            i, np = s.find(pattern), len(pattern)
            while i != -1:
                ranges.append((i, i + np))
                i = s.find(pattern, i + 1)
        ranges.sort()

        if not ranges:
            return s

        # Create windows
        dq = []
        for start, end in ranges:
            if dq and start <= dq[-1]:
                dq[-1] = max(end, dq[-1])
            else:
                dq.append(start)
                dq.append(end)

        ans, prev = [], 0
        for i in range(0, len(dq), 2):
            start, end = dq[i], dq[i + 1]
            ans.append(s[prev:start])
            ans.append(f'<b>{s[start:end]}</b>')
            prev = end
        ans.append(s[prev:])
        return ''.join(ans)


def main():
    sol = Solution()
    cases = [
        ('abc123', ["abc", "123"]),
        ('abcx123', ["abc", "123"]),
        ('abcxyz123', ["abc", "123"]),
        ('aaabbcc', ["aaa", "aab", "bc"]),
        ('xxabcdefghij', ["ab", "cd", "ef"]),
        ('abcdefghi', ["xy", "mn"]),
        (
            "qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrr"
            "czfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokz"
            "tghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaa"
            "fzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm",
            ["qr", "zj", "so", "rb", "km", "yz", "zz", "vo", "qx", "ef",
             "vx", "kc", "wt", "pk"]
        ),

    ]
    for case in cases:
        print(sol.addBoldTag(*case))


if __name__ == '__main__':
    main()

#
# @lc app=leetcode id=76 lang=python3
# [algorithms] - Hard
#
# [76] Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letter_map = {c: 0 for c in t}
        left, right = 0, 0

        best_left = 0
        best_right = len(s) + 1

        while right < len(s):
            while right < len(s) and not all(letter_map.values()):
                if s[right] in letter_map:
                    letter_map[s[right]] += 1
                right += 1
            while left < len(s) and all(letter_map.values()):
                if s[left] in letter_map:
                    letter_map[s[left]] -= 1
                left += 1
            if (right - left + 1) < (best_right - best_left):
                best_left = left - 1
                best_right = right
        if best_right - best_left > len(s):
            return ""
        return s[best_left:best_right]


def test():
    sol = Solution()
    cases = [
        # (s, t)
        ("ADOBECODEBANC", "ABCD"),
        ("ADOBECODEBANC", "XYZ"),
        ("ADOBECODEBANCDEF", "DEF"),
    ]
    for case in cases:
        print(sol.minWindow(*case))


if __name__ == "__main__":
    test()

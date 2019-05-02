"""
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
"""


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        "Return length of last word"
        i = 0
        for c in reversed(s.rstrip()):
            if c == ' ':
                break
            i += 1
        return i

    def lengthOfLastWord2(self, s: str) -> int:
        count = 0
        n = len(s) - 1
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            n -= 1
            count += 1
        return count


def test():
    "Test method"
    sol = Solution()
    cases = ["Hello World", "HelloWorld", "", "a", "a  ", "a b c"]
    for case in cases:
        assert sol.lengthOfLastWord(case) == sol.lengthOfLastWord2(case)


if __name__ == '__main__':
    test()

#
# @lc app=leetcode id=67 lang=python3
# [algorithms] - Easy
#
# [67] Add Binary
# https://leetcode.com/problems/add-binary/description/
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#


class Solution:
    def addBinary_simple(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
        return f'{int(a, 2) + int(b, 2):b}'

    def addBinary_recur(self, a: str, b: str) -> str:
        return (
            b if not a else
            a if not b else
            self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
            if (a[-1], b[-1]) == ('1', '1') else
            self.addBinary(a[:-1], b[:-1]) + '0'
            if (a[-1], b[-1]) == ('0', '0') else
            self.addBinary(a[:-1], b[:-1]) + '1'
        )

    def addBinary(self, a: str, b: str) -> str:
        result = ''
        i, carry = 0, '0'
        while i < max(len(a), len(b)) or carry == '1':
            na = a[-i - 1] if i < len(a) else '0'
            nb = b[-i - 1] if i < len(b) else '0'

            value = int(na) + int(nb) + int(carry)
            carry = '1' if value > 1 else '0'
            result = f'{value % 2}{result}'
            i += 1
        return result


def test():
    sol = Solution()
    cases = [
        ('0', '1'),
        ('001', '111'),
        ('1010', '1011'),
    ]
    for case in cases:
        print(sol.addBinary(*case))


if __name__ == '__main__':
    test()

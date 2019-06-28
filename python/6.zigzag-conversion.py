#
# @lc app=leetcode id=6 lang=python3
# [algorithms] - Medium
#
# [6] ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows in (0, 1) or numRows >= n:
            return s
        step = 2 * numRows - 2

        result = []
        for i in range(numRows):
            for j in range(i, n, step):
                result.append(s[j])
                if i in (0, numRows - 1):
                    continue
                mid = j + step - 2 * i
                if mid < n:
                    result.append(s[mid])
        return ''.join(result)

    def convert_2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        num_rows = min(numRows, len(s))
        result = [[] for _ in range(num_rows)]
        k, row_add = 0, -1

        for c in s:
            result[k].append(c)
            if k in (0, num_rows - 1):
                row_add = -row_add
            k += row_add
        return ''.join(''.join(r) for r in result)


def test():
    sol = Solution()
    cases = [
        ('AB', 1),
        ('A', 2),
        ('PAYPALISHIRING', 3),
        ('PAYPALISHIRING', 4)
    ]
    for case in cases:
        print(sol.convert(*case))


if __name__ == '__main__':
    test()

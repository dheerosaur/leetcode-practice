"""
Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.
"""
from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        answer = []
        for digit in reversed(digits):
            answer.append((digit + carry) % 10)
            carry = (digit + carry) // 10
        if carry == 1:
            return [1] + list(reversed(answer))
        return list(reversed(answer))

    def plusOne2(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(x) for x in digits))
        return [int(s) for s in str(num + 1)]

    def plusOne3(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0

        if digits[i] == 0:
            digits.insert(0, 1)
        return digits


def test():
    sol = Solution()
    cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [0],
        [9],
        [9, 9, 9],
    ]
    for case in cases:
        assert sol.plusOne(case) == sol.plusOne2(case)
        assert sol.plusOne(case) == sol.plusOne3(case)


if __name__ == '__main__':
    test()

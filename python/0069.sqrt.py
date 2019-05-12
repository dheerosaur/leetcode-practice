"""
Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.

"""
import math


class Solution:

    def mySqrt_2(self, x: int) -> int:
        "Newton's method"
        xn = x / 2
        prev = 0
        while abs(xn - prev) > 0.1:
            prev = xn
            xn = xn - (xn * xn - x) / (2 * xn)
            print(xn)
        return math.floor(xn)

    def mySqrt(self, x: int) -> int:
        return math.floor(math.sqrt(x))


def test():
    sol = Solution()
    cases = [
        124, 146, 190, 223231
    ]
    for case in cases:
        assert sol.mySqrt(case) == sol.mySqrt_2(case)


if __name__ == '__main__':
    test()

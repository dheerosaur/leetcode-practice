from typing import List


def decode_str(num):
    if num in (0, 1):
        return str(num)
    return decode(-(num >> 1)) + str(num & 1)


def decode(num):
    res = []
    while num:
        res.append(num & 1)
        num = -(num // 2)
    return res[::-1]


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1 = sum((x * (-2) ** i) for i, x in enumerate(reversed(arr1)))
        v2 = sum((x * (-2) ** i) for i, x in enumerate(reversed(arr2)))
        return decode(v1 + v2) if (v1 + v2) else [0]


def test():
    sol = Solution()
    cases = [
        ([1, 1, 1, 1, 1], [1, 0, 1]),
        ([1, 1, 0, 0, 0, 0], [1, 1, 0, 0]),
        ([1, 0, 0, 1], [1, 1, 0]),
        ([-1], [0])
    ]
    for case in cases:
        print(sol.addNegabinary(*case))


if __name__ == '__main__':
    test()

from typing import List


class Solution:
    def duplicateZeros_bf(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n - 1:
            if arr[i] == 0:
                for j in reversed(range(i + 1, n)):
                    arr[j] = arr[j - 1]
                i += 2
            else:
                i += 1
        return arr

    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        j = n + arr.count(0)

        for i in reversed(range(n)):
            j = j - 1
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j = j - 1
                if j < n:
                    arr[j] = arr[i]
        return arr


def test():
    sol = Solution()
    cases = [
        [1, 0, 2, 3, 0, 4, 5, 0],
        [1, 2, 3],
        [],
        [0],
        [1, 0],
        [0, 1],
    ]
    for case in cases:
        print(sol.duplicateZeros(case))


if __name__ == '__main__':
    test()

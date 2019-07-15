from typing import List


class Solution:
    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        for num in arr2:
            while j < len(arr1):
                if arr1[j] == num:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    i += 1
                j += 1
            j = i
        arr1[i:] = sorted(arr1[i:])
        return arr1

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda k: pos.get(k, 1000 + k))


def test():
    sol = Solution()
    cases = [
        ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
        ([2, 3, 1, 3, 2, 4], [2, 1, 4, 3, 9, 6]),
        ([2, 3, 1, 3, 44, 17], [2, 1, 4, 3]),
    ]
    for case in cases:
        print(sol.relativeSortArray(*case))


if __name__ == "__main__":
    test()

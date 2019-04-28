from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        m1 = [sum(A[i] for i in range(L))]
        for i in range(1, len(A) - L + 1):
            m1.append(m1[-1] - A[i - 1] + A[i + L - 1])

        m2 = [sum(A[i] for i in range(M))]
        for j in range(1, len(A) - M + 1):
            m2.append(m2[-1] - A[j - 1] + A[j + M - 1])

        result = -1
        for i in range(len(m1)):
            for j in range(i + L, len(m2)):
                result = max(result, m1[i] + m2[j])

        for i in range(len(m2)):
            for j in range(i + M, len(m1)):
                result = max(result, m2[i] + m1[j])
        return result


def test():
    s = Solution()
    print(s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))
    print(s.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2))
    print(s.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3))


test()

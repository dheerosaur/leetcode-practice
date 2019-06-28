from typing import List


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n, seen = sum(count), 0
        if n == 0:
            return [0.0] * 5
        if n % 2 == 0:
            m1i, m2i = n // 2, n // 2 + 1
        else:
            m1i, m2i = n // 2, n // 2
        minimum, maximum, total, m1, m2, mode_at = None, 0, 0, 0, 0, 0
        for i, ct in enumerate(count):
            if ct and minimum is None:
                minimum = i
            if ct:
                maximum = i
                total += i * ct
            if ct > count[mode_at]:
                mode_at = i
            if seen < m1i <= (seen + ct):
                m1 = i
            if seen < m2i <= (seen + ct):
                m2 = i
            seen += ct
        ans = (minimum or 0, maximum, total / n, (m1 + m2) / 2, mode_at)
        return [float(x) for x in ans]

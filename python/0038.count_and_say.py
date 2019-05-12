

class Solution:
    def countAndSay(self, n: int) -> str:
        def count_left(s, start):
            i = 1
            while (i + start) < len(s):
                if s[start + i] != s[start]:
                    break
                i += 1
            return i

        def recur(s, start):
            if start >= len(s):
                return ''
            count = count_left(s, start)
            return str(count) + s[start] + recur(s, start + count)

        nth = "1"
        for _ in range(n - 1):
            nth = recur(str(nth), 0)
        return nth


def test():
    s = Solution()
    for i in range(10):
        print(i, s.countAndSay(i))


if __name__ == '__main__':
    test()

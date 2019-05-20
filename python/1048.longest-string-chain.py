"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one
letter anywhere in word1 to make it equal to word2.  For example, "abc" is a
predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and
so on.

Return the longest possible length of a word chain with words chosen from the
given list of words.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"] Output: 4 Explanation: one of the
longest word chain is "a","ba","bda","bdca".
"""
from typing import List
import collections


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            for i in range(len(w)):
                dp[w] = max(dp.get(w, 1), dp.get(w[:i] + w[i+1:], 0) + 1)
        return max(dp.values()) if dp else 1

    def longestStrChain_bf_dp(self, words: List[str]) -> int:
        "Long winded way"
        len_map = {i: set() for i in range(1, 17)}
        for word in words:
            len_map[len(word)].add(word)

        dp = collections.defaultdict(lambda: 1)
        for n in range(1, 17):
            for nword in len_map[n]:
                for k in range(len(nword)):
                    prev = nword[:k] + nword[k+1:]
                    if prev in len_map[n-1]:
                        dp[nword] = max(dp[nword], dp[prev] + 1)
        return max(dp.values()) if dp else 1


def test():
    sol = Solution()
    cases = [
        ["a", "b", "ba", "bca", "bda", "bdca"],
    ]
    with open('./data/1048.txt') as f:
        cases.append(f.read().strip().split('\n'))
    for case in cases:
        print(sol.longestStrChain(case))


if __name__ == '__main__':
    test()

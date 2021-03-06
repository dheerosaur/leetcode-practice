#
# @lc app=leetcode id=122 lang=python3
# [algorithms] - Easy
#
# [122] Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
from typing import List


class Solution:
    def maxProfit_2(self, prices: List[int]) -> int:
        last = len(prices) - 1
        max_profit = 0
        i, valley, peak = 0, prices[0], prices[0]
        while i < last:
            while i < last and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < last and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit


def test():
    sol = Solution()
    cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
    ]
    for case in cases:
        print(sol.maxProfit_2(case))


if __name__ == '__main__':
    test()

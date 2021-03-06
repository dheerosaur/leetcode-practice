#
# @lc app=leetcode id=860 lang=python3
# [algorithms] - Easy
#
# [860] Lemonade Change
# https://leetcode.com/problems/lemonade-change/description/
#
# At a lemonade stand, each lemonade costs $5.
#
# Customers are standing in a queue to buy from you, and order one at a time
# (in the order specified by bills).
#
# Each customer will only buy one lemonade and pay with either a $5, $10, or
# $20 bill.  You must provide the correct change to each customer, so that the
# net transaction is that the customer pays $5.
#
# Note that you don't have any change in hand at first.
#
# Return true if and only if you can provide every customer with correct
# change.
#
# Input: [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
#
#
# Input: [5,5,10]
# Output: true
#
# Input: [10,10]
# Output: false
#
# Input: [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5
# bill.
# For the last customer, we can't give change of $15 back because we only have
# two $10 bills.
# Since not every customer received correct change, the answer is false.
#
# Note:
#
# 0 <= bills.length <= 10000
# bills[i] will be either 5, 10, or 20.
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
            if five < 0:
                return False
        return True


def test():
    sol = Solution()
    cases = [
        # cases
        [5, 5, 5, 10, 20],
        [5, 5, 5, 10, 10, 20, 20],
        [5, 5, 5, 5, 10, 10, 20, 20],
        [5, 5, 10],
        [10, 10],
        [5, 5, 10, 10, 20],
    ]
    for case in cases:
        print(sol.lemonadeChange(case))


if __name__ == "__main__":
    test()

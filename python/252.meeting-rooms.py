#
# @lc app=leetcode id=252 lang=python3
# [algorithms] - Easy
#
# [252] Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/description/
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false

# Input: [[7,10],[2,4]]
# Output: true
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        A = sorted(intervals)
        for i in range(len(A) - 1):
            if A[i + 1][0] < A[i][1]:
                return False
        return True


def test():
    sol = Solution()
    cases = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[1, 2], [3, 4], [5, 6]],
        [[13, 15], [1, 13]],
    ]
    for case in cases:
        print(sol.canAttendMeetings(case))


if __name__ == '__main__':
    test()

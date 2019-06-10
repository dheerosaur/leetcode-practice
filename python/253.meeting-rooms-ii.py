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
import collections
from time import time
from typing import List
from random import randrange


class Solution:
    def minMeetingRooms_bf(self, intervals: List[List[int]]) -> int:
        minutes = collections.Counter()
        for start, end in sorted(intervals):
            for i in range(start, end):
                minutes[i] += 1
        return max(minutes.values())

    def minMeetingRooms_Rooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        for start, end in intervals:
            scheduled = False
            for i, room in enumerate(rooms):
                if room[1] <= start:
                    rooms[i] = (start, end)
                    scheduled = True
                    break
            if not scheduled:
                rooms.append((start, end))
        return len(rooms)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        start_ptr, end_ptr = 0, 0
        min_rooms, num_rooms = 0, 0

        while start_ptr < len(start_times):
            if start_times[start_ptr] < end_times[end_ptr]:
                start_ptr += 1
                num_rooms += 1
                min_rooms = max(num_rooms, min_rooms)
            else:
                num_rooms -= 1
                end_ptr += 1
        return min_rooms


def get_case(n, x, y):
    return [
        sorted([randrange(x, y), randrange(x, y)])
        for _ in range(n)
    ]


def profile():
    sol = Solution()
    methods = [m for m in dir(sol) if m.startswith('minMeeting')]
    for i in range(2, 5):
        size = 10 ** i
        case = get_case(size, 0, size)
        for method in methods:
            start = time()
            getattr(sol, method)(case)
            elapsed = (time() - start) * 1e3
            print(f'{size:6} {method:25} {round(elapsed, 4)}')
        print()


def test():
    sol = Solution()
    methods = [getattr(sol, m) for m in dir(sol)
               if m.startswith('minMeeting')]
    cases = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[1, 2], [3, 4], [5, 6]],
        [[13, 15], [1, 13]],
    ]

    for case in cases:
        vals = set(m(case) for m in methods)
        assert len(vals) == 1


if __name__ == '__main__':
    test()
    # profile()

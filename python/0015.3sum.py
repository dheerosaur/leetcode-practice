import json
from collections import defaultdict


def three_sums_reverse(nums):
    reverse_map = defaultdict(list)
    answer = set()

    for i, num in enumerate(nums):
        reverse_map[num].append(i)

    length = len(nums)
    for i in range(length):
        for j in range(i, length):
            target = 0 - nums[i] - nums[j]
            for x in reverse_map[target]:
                if i != x and j != x:
                    match = tuple(sorted([nums[i], nums[j], target]))
                    answer.add(match)
    return [list(x) for x in answer]


def three_sums_bf(nums):
    "Brute force O(n^3)"
    result = set()
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if nums[i] + nums[j] + nums[k] == 0:
                    tup = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(tup)
    return [list(x) for x in result]


def test():
    with open('data/0015.json') as f:
        nums = json.loads(f.read())
        print(three_sums_reverse(nums))


if __name__ == '__main__':
    test()

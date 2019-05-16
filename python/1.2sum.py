def two_sum(nums, target):
    hmap = {}
    for i, num in enumerate(nums):
        if num in hmap:
            return [hmap[num], i]
        else:
            hmap[target - num] = i


def test():
    assert(two_sum([2, 7, 9, 10], 9) == [0, 1])
    assert(two_sum([1, 2, 3, 4], 4) == [0, 2])


if __name__ == '__main__':
    test()

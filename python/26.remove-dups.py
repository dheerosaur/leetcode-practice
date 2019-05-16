def remove_dups(nums):
    if not nums:
        return 0
    p1, p2 = 0, 0
    while p2 < len(nums):
        if nums[p2] > nums[p1]:
            p1 += 1
            nums[p1] = nums[p2]
        p2 += 1
    return p1 + 1


def test():
    assert(remove_dups([0, 0, 0, 1, 2, 3]) == 4)
    assert(remove_dups([0, 0, 1, 1, 2, 2]) == 3)


if __name__ == '__main__':
    test()

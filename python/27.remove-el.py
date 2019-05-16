
def remove_el(nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n - 1]
            else:
                i += 1
        return n


def remove_el_simple(nums, val):
    count = 0
    for n in nums:
        if n != val:
            nums[count] = n
            count += 1
    return count


def test():
    r = remove_el_simple
    assert(r([1, 2, 2, 3, 4, 5], 2) == 4)
    assert(r([1, 2, 2, 2, 2], 2) == 1)
    assert(r([], 2) == 0)
    assert(r([2], 2) == 0)


if __name__ == '__main__':
    test()

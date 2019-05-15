
def binary_search(A, t):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) / 2
        if A[mid] == t:
            return mid
        elif A[mid] > t:
            right = mid - 1
        else:
            left = mid + 1


def test():
    assert binary_search('abcdefghijh', 'd') == 3
    assert binary_search('abcdefghij', 'a') == 0
    assert binary_search('abcdefghij', 'j') == 9
    assert binary_search([1, 2, 3, 4, 5], 2) == 1
    assert binary_search([1, 2, 3], 1) == 0
    assert binary_search([1, 2, 3], 2) == 1
    assert binary_search([1, 2, 3], 3) == 2
    assert binary_search([1, 2, 3], 0) is None
    assert binary_search([1], 1) == 0


if __name__ == '__main__':
    test()

def longest_substring_window(s):
    hmap = {}
    mx = i = j = 0
    for j, c in enumerate(s):
        if c in hmap:
            i = max(hmap[c] + 1, i)
        hmap[c] = j
        j += 1
        mx = max(mx, j - i)
    return mx


def longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    last_hit = 0
    mx = current_length = 0
    hmap = {}
    for i, c in enumerate(s):
        if c in hmap:
            last_hit = max(hmap[c], last_hit)
        current_length = i - last_hit
        mx = max(mx, current_length)
        hmap[c] = i
    return mx


def test():
    l = longest_substring_window
    assert(l('abcabcd') == 4)
    assert(l('abba') == 2)
    assert(l('dheeraj') == 4)


if __name__ == '__main__':
    test()

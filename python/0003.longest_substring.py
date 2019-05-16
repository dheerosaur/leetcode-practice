def longest_substring_window(s):
    hmap = {}
    mx = i = j = 0
    for j, c in enumerate(s):
        if c in hmap:
            print(c, hmap[c], i)
            i = max(hmap[c], i)
        hmap[c] = j + 1
        mx = max(mx, j - i + 1)
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
    ll = longest_substring_window
    assert ll('abcabcd') == 4
    assert ll('abba') == 2
    assert ll('dheeraj') == 4


if __name__ == '__main__':
    test()

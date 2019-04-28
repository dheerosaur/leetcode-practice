def str_str(haystack, needle):
    pass


def str_str_2(haystack, needle):
    nl = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+nl] == needle:
            return i
    if not haystack and not needle:
        return 0


def test():
    s = str_str
    #  assert(s('hello', 'll') == 2)
    #  assert(s('abacus', 'cu') == 3)
    #  assert(s('a', '') == -1)
    #  assert(s('', '') == 0)
    #  assert(s('', 'a') == -1)
    assert(s("mississippi", "issip") == 4)


if __name__ == '__main__':
    test()

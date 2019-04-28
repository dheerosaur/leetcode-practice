def valid_parens(s):
    reverses = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if len(stack) and stack[-1] == reverses[c]:
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0


def test():
    r = valid_parens
    assert(r('[{}]') is True)
    assert(r('[[]])') is False)
    assert(r('{}') is True)
    assert(r('((()))[]{}') is True)


test()

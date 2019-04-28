def reverse_int(x):
    orig = abs(x)
    answer = 0
    mx = 2**31
    while orig > 0:
        answer = answer * 10 + orig % 10
        orig = orig // 10
    if not (-mx <= answer < mx):
        return 0
    return answer if x > 0 else -answer


def test():
    r = reverse_int
    assert(r(321) == 123)
    assert(r(-123) == -321)
    assert(r(1234567899) == 0)


test()

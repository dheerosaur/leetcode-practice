def rev(s):
    return f'{s[-1]}{rev(s[:-1])}' if s else ''
    # or rev(s[1:]) + s[0]


def print_lines(i: int):
    while i > 0:
        i, rem = divmod(i, 10)
        print(rem)


print(rev('abcdef'))
print_lines(123213)

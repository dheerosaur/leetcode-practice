def longest_common_prefix(strings):
    if len(strings) == 0:
        return ''

    prefix = strings[0]
    for string in strings[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
        if len(prefix) == 0:
            return ''
    return prefix


def longest_common_prefix_first(strings):
    if len(strings) == 0:
        return ''

    answer = strings[0]
    for string in strings[1:]:
        matched = []
        for a, b in zip(answer, string):
            if a != b:
                break
            matched.append(a)
        answer = matched
        if len(answer) == 0:
            break
    return ''.join(answer)


def test():
    l = longest_common_prefix
    assert(l(['flow', 'flower', 'flaw']) == 'fl')
    assert(l(['racecar', 'race', 'racer']) == 'race')


if __name__ == '__main__':
    test()

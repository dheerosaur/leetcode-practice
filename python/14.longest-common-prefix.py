def longest_common_prefix(strings):
    if not strings:
        return ''

    prefix = strings[0]
    for string in strings[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
        if not prefix:
            return ''
    return prefix


def longest_common_prefix_first(strings):
    if not strings:
        return ''

    answer = strings[0]
    for string in strings[1:]:
        matched = []
        for a, b in zip(answer, string):
            if a != b:
                break
            matched.append(a)
        answer = matched
        if not answer:
            break
    return ''.join(answer)


def test():
    ll = longest_common_prefix
    assert ll(['flow', 'flower', 'flaw']) == 'fl'
    assert ll(['racecar', 'race', 'racer']) == 'race'


if __name__ == '__main__':
    test()

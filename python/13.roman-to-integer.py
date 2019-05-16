specials = {
    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
    'CD': 400, 'CM': 900,
}
hmap = {
    'I': 1, 'V': 5,
    'X': 10, 'L': 50, 'C': 100,
    'D': 500, 'M': 1000
}


def roman_to_int(roman):
    total = 0
    for i, c in enumerate(roman):
        if i > 0 and hmap[c] > hmap[roman[i-1]]:
            total -= hmap[roman[i-1]] * 2
        total += hmap[c]
    return total


def roman_to_int_eval(roman):
    for k, v in specials.items():
        roman = roman.replace(k, str(v) + '+')
    for k, v in hmap.items():
        roman = roman.replace(k, str(v) + '+')
    return eval(roman + '0')


def test():
    assert(roman_to_int('III') == 3)
    assert(roman_to_int('IV') == 4)
    assert(roman_to_int('IX') == 9)
    assert(roman_to_int('LVIII') == 58)
    assert(roman_to_int('MCMXCIV') == 1994)


if __name__ == '__main__':
    test()

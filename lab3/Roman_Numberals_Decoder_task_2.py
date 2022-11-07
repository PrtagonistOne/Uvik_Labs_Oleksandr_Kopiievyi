# write your code here
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(S: str) -> int:
    _sum = 0
    for i in range(len(S) - 1, -1, -1):
        num = roman[S[i]]
        _sum = _sum - num if 3 * num < _sum else _sum + num
    return _sum


print(roman_to_int('III'))

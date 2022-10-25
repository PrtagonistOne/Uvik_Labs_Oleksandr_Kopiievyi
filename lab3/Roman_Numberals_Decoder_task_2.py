# write your code here
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(S: str) -> int:
    sum = 0
    for i in range(len(S) - 1, -1, -1):
        num = roman[S[i]]
        sum = sum - num if 3 * num < sum else sum + num
    return sum


print(roman_to_int('III'))

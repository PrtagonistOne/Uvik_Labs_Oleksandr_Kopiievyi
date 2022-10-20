# s = 'checking'
#
# s1 = s[::-1]
#
# print(s1)
#
# num1 = 1.2
# num2 = 0.2
# from decimal import Decimal
#
#
# def findProduct(x, y):  # Python function
#     if y < 0:
#         return -findProduct(x, -y)
#     elif y == 0:
#         return 0
#     elif y == 1:
#         return x
#     else:
#         return x + findProduct(x, y - 1)
#
#
# if type(num1) == float and type(num2) == float:
#     decimal_point = len(str(num1).split('.')[-1]) + len(str(num2).split('.')[-1])
#     x = int(str(num1).replace('.', ''))
#     y = int(str(num2).replace('.', ''))
#
#     z = str(findProduct(x, y))
#     zxc = ''.join(f'{val}.' if c == decimal_point else val for c, val in enumerate(z[::-1], start=1))
#
#     print(float(zxc[::-1]))
# else:
#     print(findProduct(num1, num2))

import math

print(bool(math.sqrt(4) % 1))





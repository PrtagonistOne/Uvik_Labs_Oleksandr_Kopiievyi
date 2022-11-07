# write your code here
rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

print('EBG13 rknzcyr.'.translate(rot13))

print('Guvf vf zl svefg EBG13 rkprepvfr!'.translate(rot13))

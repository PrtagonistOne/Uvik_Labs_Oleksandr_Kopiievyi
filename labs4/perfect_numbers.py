# # Perfect numbers generator
# Given the number, the task to return n perfect numbers.
#
#
# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6,
# so 6 is a perfect number. More about perfect numbers read on https://en.wikipedia.org/wiki/Perfect_number.
#
#
# Note: Use generator for that task
##
# Input: 3
# Output: 6, 28, 496

def perf_nums(nums):
    counter = 0
    for n in range(1, 1000000):
        if counter == nums:
            break
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 = sum1 + i
        if sum1 == n:
            yield n
            counter += 1


def lazy_perfect_nums(digit):
    nums = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008133952128]
    for i in range(digit):
        yield nums[i]


for i in perf_nums(4):
    print(i)

print()

for i in lazy_perfect_nums(4):
    print(i)

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


if __name__ == "__main__":
    for i in perf_nums(4):
        print(i)

    print()

    for i in lazy_perfect_nums(4):
        print(i)

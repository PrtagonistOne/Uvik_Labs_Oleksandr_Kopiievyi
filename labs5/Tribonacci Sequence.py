from functools import reduce, lru_cache


@lru_cache
def get_tribonacci(initial_sequence: tuple, n: int):
    final_sequence = list(initial_sequence)
    # Removing initial n sequence from the count
    for _ in range(n - 3):
        temp_partial = reduce(lambda x, y: x + y, initial_sequence)
        initial_sequence = initial_sequence[1:]
        initial_sequence = initial_sequence + (temp_partial,)
        final_sequence.append(temp_partial)
    return final_sequence


print(get_tribonacci((1, 1, 1), 8))
print(get_tribonacci((0, 0, 1), 9))


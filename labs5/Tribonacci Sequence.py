from functools import reduce


def tribonaka(initial_sequence: list, n: int):
    final_sequence = initial_sequence.copy()
    # Removing initial n sequence from the couґnt
    for _ in range(n-3):
        temp_partial = reduce(lambda x, y: x + y, initial_sequence)
        initial_sequence.pop(0)
        initial_sequence.append(temp_partial)
        final_sequence.append(temp_partial)
    return final_sequence


print(tribonaka([1, 1, 1], 8))
print(tribonaka([0, 0, 1], 9))

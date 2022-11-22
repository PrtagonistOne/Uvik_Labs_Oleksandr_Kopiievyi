import concurrent.futures
import os
from helpers.utils import time_track_factory, get_and_write_wordlist


@time_track_factory('Multiprocessing')
def main_multiprocessing(proc_number: int) -> None:
    with concurrent.futures.ProcessPoolExecutor(max_workers=proc_number) as executor:
        value = executor.map(get_and_write_wordlist, [f'cpu_{i}.txt' for i in range(1, proc_number + 1)])
    print(next(value), f'Amount of processes - {proc_number}')


@time_track_factory('Neither Concurrent, nor Parallel')
def main(proc_number: int) -> None:
    for i in range(1, proc_number + 1):
        get_and_write_wordlist(f'cpu_{i}.txt')


if __name__ == "__main__":
    n = os.cpu_count()
    main_multiprocessing(proc_number=n)
    main_multiprocessing(proc_number=16)
    main_multiprocessing(proc_number=32)

    main(proc_number=n)

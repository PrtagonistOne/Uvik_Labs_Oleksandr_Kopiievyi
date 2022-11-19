import concurrent.futures

from helpers.utils import time_track_factory, get_and_write_wordlist


@time_track_factory('Multiprocessing')
def main_multiprocessing(proc_number: int) -> None:
    with concurrent.futures.ProcessPoolExecutor(max_workers=proc_number) as executor:
        executor.map(get_and_write_wordlist, [f'cpu_{i}.txt' for i in range(1, n + 1)])


@time_track_factory('Neither Concurrent, nor Parallel')
def main(proc_number: int) -> None:
    for i in range(1, proc_number + 1):
        get_and_write_wordlist(f'cpu_{i}.txt')


if __name__ == "__main__":
    n = int(input("Input any n-cores number: "))  # example: 4
    main_multiprocessing(proc_number=n)  # ~4 seconds
    # main(proc_number=n)  # ~14 seconds



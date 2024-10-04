import cProfile
import pstats
from multiprocessing import Process

def find_divisors(n: int):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def main(num: int):
    if 1_000_000 <= num <= 20_000_000:
        divisors = find_divisors(num)
        print("Целочисленные делители числа", num, ":", divisors)
        return divisors
    else:
        print("Число вне допустимого диапазона.")
        return None

def run_profiled_process():
    number = 1000100
    new_process = Process(target=main, args=(number,))
    new_process.start()
    new_process.join()

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    run_profiled_process()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

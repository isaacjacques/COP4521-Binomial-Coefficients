"""

Name:Isaac Jacques
Date:2025-09-07
Assignment: Module 2: Properly Design and Build a Solution Using Threads
Due Date:2025-09-07
About this project: Computes binomial coefficients using threads and sums them
Assumptions: 
All work below was performed by Isaac Jacques

"""
import math
import argparse
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


def _worker(n_k: tuple[int, int]) -> tuple[str, int]:
    n, k = n_k
    value = math.comb(n, k)
    return (threading.current_thread().name, value)

def compute(n: int, max_workers: int = 3):
    jobs = [(n, k) for k in range(1, n + 1)]
    per_thread_sum: dict[str, int] = defaultdict(int)

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for thread_name, value in pool.map(_worker, jobs):
            per_thread_sum[thread_name] += value

    thread_total = sum(per_thread_sum.values()) + 1
    print("\nPartial sums by thread:")
    for name in sorted(per_thread_sum):
        print(f"\t{name}: {per_thread_sum[name]}")

    print(f"Total from threads: {thread_total}")
   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Computes binomial coefficients using threads and sums them")
    parser.add_argument(
        "-n", "--n",
        type=int,
        default=1000,        
        help="Calculate all combinations for k = 0 up to this number (def: 1000)"
    )
    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=3,
        help="Number of threads (def: 3)"
    )
    args = parser.parse_args()
    compute(args.n, args.workers)
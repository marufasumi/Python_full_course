import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def heavy_task(n):
    return sum(i * i for i in range(n))


n = 40_000_000
tasks = [n] * 4  # 4 identical CPU-bound tasks to parallelize


if __name__ == "__main__":
    # Sequential
    start = time.time()
    results = [heavy_task(x) for x in tasks]
    print(
        f"Sequential:      {time.time() - start:.2f}s  | results count: {len(results)}"
    )

    # Threading - no real speedup due to GIL (Global Interpreter Lock)
    start = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(heavy_task, tasks))
    print(
        f"Threading:       {time.time() - start:.2f}s  | results count: {len(results)}"
    )

    # Multiprocessing - bypasses GIL, runs in parallel across CPU cores
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_task, tasks))
    print(
        f"Multiprocessing: {time.time() - start:.2f}s  | results count: {len(results)}"
    )

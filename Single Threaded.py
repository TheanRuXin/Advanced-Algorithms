import time

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = [50, 100, 200]
    rounds = 10
    total_times = []

    for r in range(rounds):
        print(f"\n=== Round {r+1} (Single-threaded) ===")
        t1 = time.perf_counter_ns()

        for n in numbers:
            factorial(n)

        t2 = time.perf_counter_ns()
        elapsed = t2 - t1
        total_times.append(elapsed)

        print(f"Time elapsed (T) = {elapsed} ns")

    average_time = sum(total_times) / len(total_times)
    print(f"\nAverage Time (10 rounds): {average_time:.2f} ns")

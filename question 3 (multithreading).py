import threading
import time

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def calculate_factorial(n, results, index):
    factorial(n)
    results[index] = time.perf_counter_ns() #nanoseconds

if __name__ == "__main__":
    numbers = [50, 100, 200]
    rounds = 10
    total_times = []

    for r in range(rounds):
        print(f"\n=== Round {r+1} (Multithreading) ===")

        results = [0, 0, 0]
        threads = []

        t1 = time.perf_counter_ns()  # start time before any thread starts

        # Create and start 3 threads
        for i, n in enumerate(numbers):
            t = threading.Thread(target=calculate_factorial, args=(n, results, i))
            threads.append(t)
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        t2 = max(results)  # last thread to finish
        elapsed = t2 - t1
        total_times.append(elapsed)

        print(f"Time elapsed (T) = {elapsed} ns")

    average_time = sum(total_times) / len(total_times)
    print(f"\nAverage Time (10 rounds): {average_time:.2f} ns")

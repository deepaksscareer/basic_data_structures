import multiprocessing
import time

# Function with two parameters
def compute_power(base, exponent):
    print(f"[Process] Computing {base}^{exponent}")
    time.sleep(1)
    return base ** exponent

if __name__ == '__main__':
    # List of parameter tuples
    input_data = [(2, 3), (3, 2), (4, 0), (5, 1), (6, 2)]

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(compute_power, input_data)

    print("Results:", results)

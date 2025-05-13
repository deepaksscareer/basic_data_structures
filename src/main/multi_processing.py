from multiprocessing import Process

def process_name(name):
    print(f"Hello from {name}")

if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie"]
    processes = []

    for name in names:
        p = Process(target=process_name, args=(name,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


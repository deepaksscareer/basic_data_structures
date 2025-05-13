import threading
import time

# A sample function to simulate a time-consuming task
def download_file(file_id):
    print(f"[Thread {file_id}] Starting download...")
    time.sleep(2)  # Simulate time delay
    print(f"[Thread {file_id}] Download complete.")

# List to keep track of threads
# Like a cheop who keeps the list of all the tasks he need to do.
threads = []

# Create and start 5 threads
for i in range(5):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
# List the chef who keeps checking if all his taks has got completed by using the join command
for thread in threads:
    thread.join()

print("All downloads completed.")

# Setup the min heap
import heapq

class Heap:

    def __init__(self, min_heap_list, max_heap_list):
        self.min_heap_list = min_heap_list

        heapq.heapify(self.min_heap_list)

        self.max_heap_list = [ -val for val in max_heap_list]
        heapq.heapify(self.max_heap_list)

if __name__ == "__main__":
    heap = Heap(min_heap_list=[2, 1, 3, 6], max_heap_list=[10, 12, 13, 25])

    print(f"The min_Heap: {heap.min_heap_list}")
    print("Adding to min heap")
    heapq.heappush(heap.min_heap_list, -20)
    print(f"The min_Heap: {heap.min_heap_list}")
    print("------------")

    print(f"The max_Heap: {heap.max_heap_list}")
    print("Adding to max heap")
    element_add = 55
    heapq.heappush(heap.max_heap_list, -element_add)
    print(f"The max_Heap: {heap.max_heap_list}")
    print("------------")

    print("Removing from min heap and printing")
    while len(heap.min_heap_list) > 0:
        
        removed_element = heapq.heappop(heap.min_heap_list)
        print(f"Removed Element: {removed_element}")
        print(f"New list: {heap.min_heap_list}")
    print("------------")

    print("Removing from max heap and printing")
    while len(heap.max_heap_list) > 0:
        
        removed_element = heapq.heappop(heap.max_heap_list)
        print(f"Removed Element: {-removed_element}")
        print(f"New list: {heap.max_heap_list}")
    print("------------")    
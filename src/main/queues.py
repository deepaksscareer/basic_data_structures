# Creation of the queue
from collections import deque
# Not thread safe approach
import queue  # For Thread safe approach.


class TaskAction:

    def __init__(self):
        # Create queue
        self.task_queue = deque()

    def print_element(self):
        """
        Show data
        """

        # Edge case:
        if len(list(self.task_queue)) == 0:
            print("No elements!!")

        for element in list(self.task_queue):
            if element:
                print(f"Given element : {element}")


if __name__ == "__main__":
    task = TaskAction()

    # Adding element
    task.task_queue.append("eating")
    task.task_queue.append("sitting")
    task.task_queue.append("receiving")
    print(task.print_element())
    print("-----------------------------")

    task.task_queue.pop()
    # Removing element from top
    print(task.print_element())
    print("-----------------------------")

    task.task_queue.append("playing")
    task.task_queue.popleft()
    # Removing element from top
    print(task.print_element())
    print("-----------------------------")

    # Print size of queue
    print(f"No tasks : {len(task.task_queue)}")

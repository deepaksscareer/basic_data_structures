from collections import deque
class Node:

    def __init__(self, data):
        
        self.data = data
        self.left_node = None
        self.right_node = None

class BinaryTree:

    def __init__(self):
        self.header = None

        self.insert_q = deque()


    def insert_element(self, value):
        """
        Always add the elemnt from left to right
        Time complexity to add O(N)
        """
        given_node = Node(data=value)

        # Else start insertion
        def _insert():

            # Edge cases
            # If queue is empty, then ...
            if len(self.insert_q) == 0:
                print(f"Starting point")
            else:
                # While the quey is not empty perform the operation:                
                while len(self.insert_q) > 0:
                    # Remove last element.
                    last_element: Node = self.insert_q.popleft()

                    # If left value for element is not available, then add the element to the left and return
                    if not last_element.left_node:
                        last_element.left_node = given_node
                        return
                    else:
                        self.insert_q.append(last_element.left_node)
                    
                    # IF the right value for the element is not available, then add to the right and return
                    if not last_element.right_node:
                        last_element.right_node = given_node
                        return
                    else:
                        self.insert_q.append(last_element.right_node)

        # Edge
        # If header is not available, then add here
        if not self.header:
            self.header = given_node
        else:
            self.insert_q.appendleft(self.header)
            _insert()

    def print_tree(self):

        """
        In order tranversal
        """

        def _print(root: Node):
            
            # Edge condition of root exists
            if root:
                # Go to left
                _print(root=root.left_node)

                # Print current
                print(f"{root.data}", end=" -> ")

                # Go to right
                _print(root=root.right_node)

        _print(root=self.header)


if __name__ == "__main__":

    bin_tree = BinaryTree()

    bin_tree.insert_element(1)
    bin_tree.insert_element(3)
    bin_tree.insert_element(5)
    bin_tree.insert_element(2)
    bin_tree.insert_element(8)

    bin_tree.print_tree()            
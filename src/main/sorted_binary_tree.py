
class Node:

    def __init__(self, data):
        
        self.data = data
        self.left_node = None
        self.right_node = None
    
class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, input):
        
        """
        Insert the element
        """
        self.node = Node(data=input)

        def _insert(root: Node, input):

            # If the end is reached, then add the value
            if root is None:
                return self.node
            
            # If current value is less than root, go to the left
            if input < root.data:
                root.left_node = _insert(root=root.left_node, input=input)

            # If current value is greater than root, go to the right
            else:
                root.right_node = _insert(root=root.right_node, input=input)

            return root

        self.root = _insert(root=self.root, input=input)

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

        _print(root=self.root)

if __name__ == "__main__":

    bin_tree = BinaryTree()
    bin_tree.insert(1)
    bin_tree.insert(3)
    bin_tree.insert(5)
    bin_tree.insert(2)

    bin_tree.print_tree()
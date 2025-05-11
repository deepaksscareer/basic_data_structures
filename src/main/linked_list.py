
class Node:

    def __init__(self, data):
        
        self.data = data
        self.next_node = None
    
    def __str__(self):
        print(f"Value: {self.data}")

class LinkedList:

    def __init__(self):
        self.header = None

    def append_element(self, value):
        """
        Append an element to the linked list
        """
        # Make node
        node = Node(data=value)

        # Edge case
        # If header is none. 
        # Make the current node to point from header
        if not self.header:
            self.header = node
            return
            
        current_node = self.header

        # Normal case
        # Reach till the last point where next node is not there
        while current_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = node

    def print_list(self):
        """
        Print the elemnts on the linked list
        """
        current_node = self.header

        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        
        print("None")

    def find(self, element):
        """
        Check if the element exists
        """
        current_node = self.header
        counter = 0

        while current_node:
            if current_node.data == element:
                return(f"{element} is available at location {counter}")
                return
            
            counter += 1
            current_node = current_node.next_node
    
        return(f"{element} is not available!!")

    def delete_element(self, element):
        """
        Check if the element exists and if so, then delete the element
        """
        current_node = self.header
        prev_node = None

        # Edge cases if the hader is the value
        if current_node and current_node.data == element:
            # Removing the header
            self.header = current_node.next_node
            return
        
        # Search till the key is not available
        while current_node and current_node.data != element:
            prev_node = current_node
            current_node = current_node.next_node

        # IF the end is reached, then say cannot delete
        if not current_node:
            print(f"The key {element} does not exists")
            return
        
        prev_node.next_node = current_node.next_node


if __name__ == "__main__":
    link_list = LinkedList()

    link_list.append_element(value=10)
    link_list.append_element(value=20)
    link_list.append_element(value=30)
    link_list.print_list()

    assert link_list.find(element=10) == "10 is available at location 0"
    assert link_list.find(element=30) == "30 is available at location 2"
    assert link_list.find(element=50) == "50 is not available!!"

    print(link_list.delete_element(30))
    
    link_list.print_list()


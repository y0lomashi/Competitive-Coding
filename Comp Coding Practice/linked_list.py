
# * In notebook

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.headval = None
    # Iteratre through the linked list and print values
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next


# create a linked list
list1 = LinkedList()
list1.headval = Node(3)
# or you can create variables for each node and make the next value of the 
# previous node the new node
list1.headval.next = Node(4)
list1.headval.next.next = Node(5)

list1.print_list()



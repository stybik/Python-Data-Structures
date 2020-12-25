class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self, ref_node):
        current = self.head
        while(current and current.next != ref_node):
            current = current.next
        return current

    def display(self):
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next


def remove_duplicate(llist):
    current1 = llist.head
    while(current1):
        data = current1.data
        current2 = current1.next
        while(current2):
            if current2.data == data:
                llist.remove(current2)
            current2 = current2.next
        current1 = current1.next


l_list = LinkedList()
data_list = input(f"Please enter a linked list: ").split()

for data in data_list:
    l_list.append(int(data))

remove_duplicate(l_list)

print("List with duplicated removed")

l_list.display()

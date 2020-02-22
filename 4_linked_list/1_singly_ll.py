class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Push in front of the linked list
    def push_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print("Inserted {} at first".format(new_data))

    # insert after a given node
    def push_after(self, prev_node, new_data):
        temp = self.head
        while(temp.data != prev_node):
            temp = temp.next

        new_node = Node(new_data)
        new_node.next = temp.next
        temp.next = new_node
        print("Inserted {} at after {}".format(new_data, prev_node))

    # insert at the end
    def push_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        new_node.next = None

    def sorted_insert(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head
            while(current.next is not None and current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def delete_node(self, ele):
        temp = self.head

        if(temp.data == ele):
            if temp.next is not None:
                temp.data = temp.next.data
                temp.next = temp.next.next
            else:
                print("There is only one node, lis cannot be empty")
            return

        while(temp.next is not None and temp.next.data != ele):
            temp = temp.next

        if temp.next is None:
            print("Given node is not present")

        else:
            temp.next = temp.next.next
    

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    llist = LinkedList()

    elements = [int(i) for i in input().split()]
    for i in elements:
        llist.push_end(i)

    llist.delete_node(3)

    print("Created Linked list is ")
    llist.printList()

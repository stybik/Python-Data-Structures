class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None

    def push_end(self, new_data):
        new_node = Node(new_data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node
        return self.head

    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if(temp == self.head):
                    break

if __name__ == "__main__":

    head = None
    llist = CircularLL()
    elements = [int(i) for i in input().split()]
    for i in elements:
        head = llist.push_end(i)
    
    print("Created Linked list is ")
    llist.printList()
    print("Head", head)
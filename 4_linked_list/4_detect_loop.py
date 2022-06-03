class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return

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
    
    print("Created Linked list is ")
    llist.printList()

    llist.head.next.next.next.next = llist.head
    llist.detect_loop()
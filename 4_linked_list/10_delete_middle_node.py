class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
  
    # Method to initialize head 
    def __init__(self): 
        self.head = None

    # Method to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data)
        if self.head is None:
                self.head = new_node
                return
        
        curr = self.head
        while(curr.next):
            curr = curr.next

        curr.next = new_node
        new_node.next = None


    # Method function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next

    def deleteMid(self):
        if (self.head is None) or (self.head.next is None):
            return

        slow_ptr = self.head
        fast_ptr = self.head

        prev = None

        while(fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next



if __name__ == "__main__":
    ele = [int(i) for i in input().split()]
    llist = LinkedList()
    for i in ele:
        llist.push(i)

    print("Given linked list")
    llist.printList()

    llist.deleteMid()

    print()
    print("Linked List after deleting middle node: ")
    llist.printList()
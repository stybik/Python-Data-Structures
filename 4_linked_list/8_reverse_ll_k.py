class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next

    # utility function to reverse the linked list by k positions
    def reverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1 

        if next is not None:
            head.next = self.reverse(next, k)

        return prev


if __name__ == "__main__":
    ele = [int(i) for i in input().split()]
    llist = LinkedList()
    for i in ele:
        llist.push(i)

    print("Given linked list")
    llist.printList()

    llist.head = llist.reverse(llist.head, 3)

    print("\Reversed list by k elements")
    llist.printList()

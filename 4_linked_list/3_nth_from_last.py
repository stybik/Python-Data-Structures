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

    def find_last(self, pos):
        main = self.head
        ref = self.head

        count = 0
        if(self.head is not None):
            while(count < pos):
                if(ref is None):
                    print("invalid input")
                    return
                ref = ref.next
                count+=1

            while(ref is not None):
                main = main.next
                ref = ref.next
            
            print("Nth node from last is {}".format(main.data))
                
                

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

    n = int(input("Enter position from last: "))
    llist.find_last(n)
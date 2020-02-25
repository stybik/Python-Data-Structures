class LinkedList:

    def __init__(self):
        self.head = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def merge(self, q):
        p_curr = self.head
        q_curr = q.head 
        while(p_curr and q_curr):
            p_next = p_curr.next
            q_next = q_curr.next

            q_curr.next = p_next
            p_curr.next = q_curr

            p_curr = p_next
            q_curr = q_next
        q.head = q_curr

    def print_list(self):
        temp = self.head
        while(temp):
            print(str(temp.data))
            temp = temp.next
        print(" ")

llist1 = LinkedList()
llist2 = LinkedList()

llist1.push(3)
llist1.push(2)
llist1.push(1)

print("First list: ")
llist1.print_list()

llist2.push(8)
llist2.push(7)
llist2.push(6)
llist2.push(5)
llist2.push(4)

print("Second List: ")
llist2.print_list()

llist1.merge(llist2)

print("modified 1st list: ")
llist1.print_list()

print("Modified 2nd list: ")
llist2.print_list()
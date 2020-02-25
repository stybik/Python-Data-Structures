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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def compare(list1, list2):
    while(list1 and list2 and list1.data == list2.data):
        list1 = list1.next
        list2 = list2.next

    if(list1 and list2):
        return 1 if list1.data > list2.data else -1

    if (list1 and not list2):
        return 1

    if (list2 and not list1):
        return -1

    return 0

if __name__ == "__main__":
    
    list1 = [i for i in input()]
    list2 = [i for i in input()]

    llist1 = LinkedList()
    llist2 = LinkedList()
    c = LinkedList()

    for i in list1:
        llist1.push_end(i)

    for i in list2:
        llist2.push_end(i)

    llist1.printList()
    llist2.printList()
    print(compare(llist1, llist2))

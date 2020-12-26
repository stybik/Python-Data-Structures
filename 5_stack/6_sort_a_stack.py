def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        print("Empty Stack")
    else:
        stack.pop()

def top(stack):
    return stack[-1]

def printStack(stack):
    for i in stack:
        print(i, end=" ")

def sortStack(stack):
    temp_stack = createStack()
    while(isEmpty(stack) == False):
        temp = top(stack)
        pop(stack)

        while(isEmpty(temp_stack) == False and top(temp_stack) > temp):
            push(stack, top(temp_stack))
            pop(temp_stack)

        push(temp_stack, temp)
    return temp_stack

if __name__ == "__main__":
    stack = createStack()   
    elements = [int(i) for i in input().split()]
    for ele in elements:
        push(stack, ele)
    print("Stack before sorting: ")
    printStack(stack)
    print("Stack after sorting: ")
    sortedStack = sortStack(stack)
    printStack(sortedStack)
class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Stack:
    return Stack()
    # raise NotImplementedError("Stack.initialize() not defined")


def isEmpty(data: Stack) -> bool:
    return data.first == None
    # raise NotImplementedError("Stack.isEmpty() not defined")


# add in front of head
def push(data: Stack, value: int) -> Stack:
    data.first = Node(value, data.first)
    return data
    # raise NotImplementedError("Stack.push() not defined")


# remove first node, and return rest of stack with the removed node
def pop(data: Stack) -> tuple[Node, Stack]:
    newnode = data.first
    data.first = data.first.next
    
    # return as tuple
    return [newnode, data]
    # raise NotImplementedError("Stack.pop() not defined")


def peek(data: Stack) -> Node:
    return Node(data.first.value, None)
    # raise NotImplementedError("Stack.peek() not defined")


def clear(data: Stack) -> Stack:
    data.first = None
    return data
    # raise NotImplementedError("Stack.clear() not defined")
    
    
"""l = initialize()
l = push(l, 2)
print(peek(l).value)"""
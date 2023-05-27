class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
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


def initialize() -> Queue:
    return Queue()
    # raise NotImplementedError("Queue.initialize() not defined")


def isEmpty(data: Queue) -> bool:
    return data.first == None
    # raise NotImplementedError("Queue.isEmpty() not defined")


# add node to the back
def enqueue(data: Queue, value: int) -> Queue:
    def helper(current: Node):
        # base case #1 if there's nothing in the list
        if current is None:
            data.first = Node(value, None) # can use value var because it's inside the main function
            return data
        # base case #2 if the next node points to None
        if current.next is None:
            current.next = Node(value, None)
            return data
        
        # loop until you get through all the nodes in the list
        helper(current.next)
        
    # if there are nodes in the list already, loop through all the nodes
    helper(data.first)
    
    return data
    # raise NotImplementedError("Queue.enqueue() not defined")


# return the front of the node and then the rest of it
def dequeue(data: Queue) -> tuple[Node, Queue]:
    newnode = data.first
    data.first = data.first.next
    
    # return as tuple
    return [newnode, data]
    # raise NotImplementedError("Queue.dequeue() not defined")


def peek(data: Queue) -> Node:
    return Node(data.first.value, None)
    # raise NotImplementedError("Queue.peek() not defined")


def clear(data: Queue) -> Queue:
    data.first = None
    return data
    # raise NotImplementedError("Queue.clear() not defined")
    
    
"""l = initialize()
l = enqueue(l, 5)
l = enqueue(l, 432)
print(Queue.toPythonList(l))"""
class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    return List()
    # raise NotImplementedError("List.initialize() not defined")


def isEmpty(data: List) -> bool:
    return data.first == None
    # raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(current: Node, count: int):
        # if you want to add it to the front
        if index == 0:
            addToFront(data, value)
            return data
        # if the index is somewhere in the middle to the end
        if count == index:
            current.next = Node(value, current.next)
            return data
        # loop until you get through all the nodes in the list, make sure that the next node is not None before looping
        if current.next is not None:
            helper(current.next, count + 1)
        
    # make sure the index is possible
    if len(data) <= index or index < 0:
        raise ValueError("IMPOSSIBLE!")
    
    # if there are nodes in the list already, loop through all the nodes
    helper(data.first, 1)
    
    return data
    # raise NotImplementedError("List.addAtIndex() not defined")


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(current: Node, count: int) -> Node:
        global last
        
        # base case #1 if there's only one element in the list, make it the head of the List
        if index == 0:
            data.first = current.next
            return current
        
        # base case #2
        if count == index:
            val = last.next.value
            last.next = last.next.next
            return Node(val, None)
        
        # loop until you get through all the nodes in the list
        last = current
        return helper(current.next, count + 1)
        
    # make sure the index is possible
    if len(data) <= index or index < 0 or isEmpty(data) == True:
        raise ValueError("IMPOSSIBLE!")

    # return as tuple
    return [helper(data.first, 0), data]
    # raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    data.first = Node(value, data.first)
    return data
    # raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
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
    # raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:
    def helper(current: Node, count: int) -> Node:
        # base case once node at index is found
        if index == count:
            return Node(current.value, None)
        
        # loop until you get to the node index
        # MUST RETURN THE NODE
        return helper(current.next, count + 1)
    
    # make sure the index is possible
    if len(data) <= index or index < 0:
        raise ValueError("IMPOSSIBLE!")

    # if there are nodes in the list already, loop through all the nodes
    return helper(data.first, 0)
    # raise NotImplementedError("List.getElementAtIndex() not defined")


def clear(data: List) -> List:
    data.first = None
    return data
    # raise NotImplementedError("List.clear() not defined")


"""l = initialize()
print("")
l = addToFront(l, 69)
l = addToBack(l, 0)
l = addToBack(l, 68)
l = addToBack(l, 1)
l = addToBack(l, 2)
l = addAtIndex(l, 1, 22)
print(l.toPythonList())
n, l = removeAtIndex(l, 4)
print(n.value, 'removed')
x = getElementAtIndex(l, 3)
print(x.value, 'is the value')
print(l.toPythonList(), 'after')
print("")"""
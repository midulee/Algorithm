class Stack:
    def __init__(self, initial=[]):
        self.members = initial

    def push(self, new):
        self.members.append(new)

    def pop(self):
        return self.members.pop()

    def top(self):
        print(self.members[-1])

    def empty(self):
        if self.members:
            return False
        return True

    def size(self):
        return len(self.members)

    def print(self):
        print(" ".join(map(str, self.members)))


class Dequeue:
    def __init__(self):
        self.members = []

    def push_front(self, value):
        self.members.append(value)

    def push_back(self, value):
        self.members.insert(0, value)

    def pop_front(self):
        return self.members.pop()

    def pop_back(self):
        return self.members.pop(0)

    def front(self):
        return self.members[-1]

    def back(self):
        return self.members[0]

    def empty(self):
        if self.members:
            return True
        return False

    def size(self):
        return len(self.members)


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def remove(self, value):
        if self.head.data == value:
            self.head = self.head.next
        else:
            prev = self.head
            node = prev.next
            while node:
                if node.data == value:
                    prev.next = node.next
                    break
                prev = node
                node = node.next

        self.size -= 1

    def print_list(self):
        node = self.head
        if node:
            output = node.data
            node = node.next
        while node:
            output = "{}->{}".format(output, node.data)
            node = node.next
        print(output)

    def get_size(self):
        return self.size


class Heap:
    '''
    Max Heap data structure implementation using array
    '''

    def __init__(self, initial=[]):
        self.members = initial

    def add(self, value):
        self.members.append(value)
        self.alignUp()
        self.print()

    def getRoot(self):
        return self.members[0]

    def isEmpty(self):
        if self.members:
            return False
        return True

    def pop(self):
        if self.isEmpty():
            print("Heap is empty, no member left to pop")
            return

        root = self.members[0]
        self.members[0] = self.members.pop()
        self.alignDown()
        return root

    def print(self):
        print(self.members)

    def alignUp(self):
        last = len(self.members) - 1
        parent = (last - 1) // 2
        while parent >= 0 and self.members[last] < self.members[parent]:
            self.members[parent], self.members[last] = self.members[last], self.members[parent]
            last = parent
            parent = (last - 1) // 2


    def alignDown(self):
        index = 0
        left = index * 2 + 1
        right = index * 2 + 2
        while (left and right) < len(self.members) and (self.members[index] > self.members[left] or self.members[index] > self.members[right]):
            if self.members[left] < self.members[right]:
                self.members[index], self.members[left] = self.members[left], self.members[index]
                index = left
            else:
                self.members[index], self.members[right] = self.members[right], self.members[index]
                index = right
            left = index*2 + 1
            right = index*2 + 2

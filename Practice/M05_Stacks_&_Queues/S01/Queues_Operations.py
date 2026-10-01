'''
Queues: Queue is a linear DS which follows FIFO (First In First Out)

Operations:
1. Enqueue: Insert the data 
2. Dequeue: Remove the data
3. Peek: Get the top element of the queue
4. is_empty: Check if the queue is empty

Keywords:
1. front: starting of the queue
2. rear: ending of the queue

Implementations:
1. Using List 
2. Using Linked List
'''
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

s = Queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
print(s.items)
print(s.dequeue())
print(s.peek())
print(s.is_empty())
print(s.size())

'''USING LINKED LIST'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    def peek(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data
    def is_empty(self):
        return self.front is None
    
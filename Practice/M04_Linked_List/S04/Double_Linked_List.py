'''
Double Linked List:
'''
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 
def insert_at_head(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insert_after_pos(node,data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.next = node.next
    new_node.prev = node
    if node.next:
        node.next.prev = new_node
    node.next = new_node

def insert_before_pos(node,data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node
    if node.prev:
        node.prev.next = new_node
    node.prev = new_node

def traverse(head):
    curr = head 
    while curr:
        print(curr.data, end='<->')
        curr = curr.next
    print("None")
head = None 
head = insert_at_head(head, 10)
head = insert_at_head(head, 20)
head = insert_at_head(head, 30)
print("Insertion at begin:")
traverse(head)
print()
insert_after_pos(head.next, 40)
traverse(head)
insert_before_pos(head.next, 50)
traverse(head)
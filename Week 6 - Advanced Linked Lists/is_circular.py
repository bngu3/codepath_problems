class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    # edge case if we have an empty list 
    if not head:
        return False
    
    current = head.next
    while current and current != head:
        current = current.next

    return current == head

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)

num1.next = num2
num2.next = num3
num3.next = num1
# num1 -> num2 -> num3 -> num1
print(is_circular(num1))

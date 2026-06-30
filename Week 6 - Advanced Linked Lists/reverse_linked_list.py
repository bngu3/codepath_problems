class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def reverse(head):
    prev = None
    current = head

    while current is not None:
        nxt = current.next
        current.next = prev
        
        prev = current
        current = nxt
    return prev



head = Node(1,Node(2, Node(3, Node(4, Node(5)))))
print_list(head)
print_list(reverse(head))

# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1
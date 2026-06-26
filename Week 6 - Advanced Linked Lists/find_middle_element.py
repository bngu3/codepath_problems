class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = head
    fast = head

    while fast and fast.next: # whenever we stop, slow should be at middle
        slow = slow.next
        fast = fast.next.next

    return slow

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next 
        
    print("None")

head = Node(1,Node(2, Node(3)))

middle_node = find_middle_element(head)
print(middle_node.value)

# Input List:
# 1 -> 2 -> 3
# Input: head = 1


# Expected Return Value: 2
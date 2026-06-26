class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True
    
    slow = head
    fast = head

    while fast and fast.next: # whenever we stop, slow should be at middle
        slow = slow.next
        fast = fast.next.next

    second_half = reverse(slow)
    first_half = head

    while second_half is not None:
        if first_half.value != second_half.value:
            return False  
        first_half = first_half.next
        second_half = second_half.next
    return True

def reverse(head):
    prev = None
    current = head

    while current is not None:
        nxt = current.next
        current.next = prev

        prev = current
        current = nxt
    return prev

# Input List:
# 1 -> 2 -> 1
# Input: head = 1

# True
head = Node(1,Node(2,Node(1)))
print(is_palindrome(head))
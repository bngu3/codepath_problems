class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
    less_dummy = Node(0)
    greater_dummy = Node(0)

    less = less_dummy # basically head for less list
    greater = greater_dummy # basically head for greater list

    current = head

    while current:
        if current.value < val:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    less.next = greater_dummy.next

    greater.next = None
    return less_dummy.next

def create_linked_list(arr):
    """Helper function to turn a Python list into a Linked List."""
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    """Helper function to visualize the linked list as a string."""
    elements = []
    current = head
    while current:
        elements.append(str(current.value))
        current = current.next
    print(" -> ".join(elements) if elements else "Empty List")

test_head = create_linked_list([1, 4, 3, 2, 5, 2])
target_val = 3

print("Original Linked List:")
print_linked_list(test_head)

partitioned_head = partition(test_head, target_val)

print("Resulting Linked List:")
print_linked_list(partitioned_head)


     

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
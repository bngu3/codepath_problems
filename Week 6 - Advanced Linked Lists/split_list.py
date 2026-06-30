class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def split_odd_even(head):
    # 1. Create a dummy node for your odd list AND your even list
    odd_dummy = Node(0)
    even_dummy = Node(0)
    
    # 2. Create your two builder pointers (tails)
    odd_tail = odd_dummy
    even_tail = even_dummy
    
    # 3. Create your scanner pointer
    current = head
    
    # 4. Your loop goes here!
    # - Check the value inside the box
    # - Attach the ENTIRE box (current) to the correct tail
    # - Move that specific tail forward
    # - Move your scanner forward
    while current is not None:
        # even case
        if current.value % 2 == 0:
            even_tail.next = current
            even_tail = even_tail.next
        else:
            odd_tail.next = current
            odd_tail = odd_tail.next
        current = current.next
    odd_tail.next = None
    even_tail.next = None
    return odd_dummy.next, even_dummy.next

# --- Test Code ---
# Input List: 1 -> 2 -> 3 -> 4 -> 5
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)

# Run your function (should return a tuple of the two lists)
odd_head, even_head = split_odd_even(head)

# Print Helper function
def print_list(node):
    out = []
    while node:
        out.append(str(node.value))
        node = node.next
    print(" -> ".join(out) if out else "None")

print("Odds: ", end="")
print_list(odd_head)   # Expected: 1 -> 3 -> 5

print("Evens: ", end="")
print_list(even_head)  # Expected: 2 -> 4
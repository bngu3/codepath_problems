class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def filter_evens(head):
    # 1. Create your dummy node here: dummy = Node(0)
    # 2. Create a pointer to track the tail of your new list
    # 3. Loop through the original list
    # 4. If a value is even (val % 2 == 0), attach a new Node to your tail

    dummy = Node(0)
    tail = dummy
    current = head

    while current is not None:
        if current.value % 2 == 0:
            tail.next = current
            tail = tail.next
        current = current.next
        
    tail.next = None
    return dummy.next

        

# --- Test Code ---
# Input List: 1 -> 4 -> 3 -> 6 -> 8
n5 = Node(8)
n4 = Node(6, n5)
n3 = Node(3, n4)
n2 = Node(4, n3)
head = Node(1, n2)

# Run your function
even_head = filter_evens(head)

# Print helper (Expected Output: 4 -> 6 -> 8)
current = even_head
output = []
while current:
    output.append(str(current.value))
    current = current.next
print(" -> ".join(output) if output else "None")
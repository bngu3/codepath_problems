class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def reverse_between(head, m, n):
    if not head or m == n:
        return head
    
    dummy = Node(0)
    dummy.next = head # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    prev = dummy

    # stops at the node before our target node
    for _ in range(m - 1): 
        prev = prev.next

    current = prev.next 

    sub_prev = None
    sub_curr = current

    for _ in range(n - m + 1):
        nxt = sub_curr.next
        sub_curr.next = sub_prev

        sub_prev = sub_curr
        sub_curr = nxt

    current.next = sub_curr # Makes 2 point to None
    prev.next = sub_prev

    return dummy.next
# 1 -> 2 -> 3 -> 4 -> 5

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
head = Node(1, n2)

# Reverse between position 2 and 5 (1-based index)
result_head = reverse_between(head, 2, 5)

# Print helper
# Expected output: 1 -> 5 -> 4 -> 3 -> 2
current = result_head
output = []
while current:
    output.append(str(current.value))
    current = current.next
print(" -> ".join(output))
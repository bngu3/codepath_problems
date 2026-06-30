class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    current_a = head_a
    current_b = head_b

    dummy = Node(0)
    result = dummy
    
    carry = 0
    while current_b is not None and current_a is not None:
        val_a = current_a.value if current_a is not None else 0
        val_b = current_b.value if current_b is not None else 0

        column_sum = val_a + val_b + carry
        carry = column_sum // 10
        result.next = Node(column_sum % 10)
        result = result.next

        if current_a is not None:
            current_a = current_a.next
        if current_b is not None:
            current_b = current_b.next
    return dummy.next


a3 = Node(3)
a2 = Node(4, a3)
head_a = Node(2, a2)

b3 = Node(4)
b2 = Node(6, b3)
head_b = Node(5, b2)

result_head = add_two_numbers(head_a, head_b)

current = result_head
output_list = []
while current:
    output_list.append(str(current.value))
    current = current.next

print(" -> ".join(output_list))


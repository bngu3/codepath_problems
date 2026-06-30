class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_last_node_in_cycle(head):
    if not head:
        return None
        
    visited = set()
    current = head

    while current:
        if current.next in visited:
            return current
        
        visited.add(current)
        current = current.next
    return None

    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # detect if we have a cycle
        if slow == fast:
            break
        # no cycle detected
        else:
            return None
        
    fast = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow

    current = cycle_start
    while current.next != cycle_start:
        current = current.next
        
    return current
    """




num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)


num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

result = find_last_node_in_cycle(num1)
print(result.value)
#Example Input: num1 -> num2 -> num3 -> num4 -> num2

#Example Output: num4
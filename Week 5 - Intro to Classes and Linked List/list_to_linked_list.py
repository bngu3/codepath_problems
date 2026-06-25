class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    head = Node(lst[0])
    current = head
    for item in lst[1:]:
        new_node = Node(item)
        current.next = new_node
        current = current.next
    return head



normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)


# This prints ONLY the head node's value:
print(linked_list.value)   # => "Betty"

# (Optional) Traverse to print the whole linked list:
current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next


# Print the head node's VALUE:
print(linked_list.value)        # expected: Betty

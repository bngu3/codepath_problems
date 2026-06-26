class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	current = head
	counter = 0
	while current is not None:
		if current.value == val:
			counter += 1
		current = current.next # make sure this it out of block so it goes to the next node 
	return counter


test_list = Node(3, Node(1, Node(2, Node(1))))
target_value = 1
result = count_element(test_list, target_value)
print(result)
# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
# 2
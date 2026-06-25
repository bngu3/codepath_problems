class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
    
head = Node(4, Node(3, Node(2)))

current = head
while current is not None:
	if current.next is not None:
		print(current.value, end=" -> ")
	else:
		print(current.value)
	current = current.next
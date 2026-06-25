class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")

poliwag.next = poliwhirl
poliwag.prev = None

poliwhirl.next = poliwrath
poliwhirl.prev = poliwag

poliwrath.next = None
poliwrath.prev = poliwhirl

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)


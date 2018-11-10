import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def check_cycle(head):
	slow, fast = head, head
	while (True):
		if (fast.data == slow.data):
			return fast
		slow = slow.next
		fast = fast.next.next
		
	
class TestClass(unittest.TestCase):
	def test_cycle(self):
		n0 = Node(0)
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		n3.append(n0)
		
		self.assertEqual(check_cycle(n0), n0)
		
		
if __name__ == '__main__':
	unittest.main()
	
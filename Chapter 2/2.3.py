import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def delete_mid(n):
	n.data = n.next.data
	n.next = n.next.next
		
class TestClass(unittest.TestCase):
	def test_delete_mid(self):
		n0 = Node(0)
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		n4 = Node(4)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		n3.append(n4)
		
		delete_mid(n2)
		self.assertEqual(n2.data, 3)
		self.assertEqual(n2.next, n4)
		
if __name__ == '__main__':
	unittest.main()
	
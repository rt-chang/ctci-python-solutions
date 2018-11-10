import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def find_kth_last(head, k):
	target, offset = head, head
	for i in range(k):
		if (not offset):
			raise Exception("Invalid k value")
		offset = offset.next
	
	while offset:
		target = target.next
		offset = offset.next
	
	return target
			
		
class TestClass(unittest.TestCase):
	def test_find_kth(self):
		n0 = Node(0)
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		
		self.assertEqual(find_kth_last(n0, 1), n3)
		self.assertEqual(find_kth_last(n0, 2), n2)
		
		n10 = Node(0)
		self.assertEqual(find_kth_last(n10, 0), None)
		self.assertEqual(find_kth_last(n10, 1), n10)
		
	def test_exceptions(self):
		with self.assertRaises(Exception):
			 find_kth_last(None, 5)
		
if __name__ == '__main__':
	unittest.main()
	
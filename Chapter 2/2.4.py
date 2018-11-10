import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def partition_list(head, v):
	if (not head):
		return None
		
	l1_head, l1_tail = None, None
	l2_head, l2_tail = None,  None
	curr = head
	
	while curr:
		if (curr.data < v):
			if l1_head:
				l1_tail.next = curr
				l1_tail = l1_tail.next
			else:
				l1_head, l1_tail = curr, curr
		else:
			if l2_head:
				l2_tail.next = curr
				l2_tail = l2_tail.next
			else:
				l2_head, l2_tail = curr, curr
		curr = curr.next
	
	l1_tail.next = l2_head
	return l1_head
		
	
class TestClass(unittest.TestCase):
	def test_partition_list(self):
		n0 = Node(4)
		n1 = Node(3)
		n3 = Node(1)
		n2 = Node(3)
		n4 = Node(2)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		n3.append(n4)
		
		partitioned = partition_list(n0, 3)
		self.assertEqual(partitioned.data, 1)
		self.assertEqual(partitioned.next.data, 2)
		self.assertEqual(partitioned.next.next.data, 4)
		self.assertEqual(partitioned.next.next.next.data, 3)
		self.assertEqual(partitioned.next.next.next.next.data, 3)
		
	def test_empty_list(self):
		self.assertEqual(partition_list(None, 2), None)
		
	def test_value_at_start(self):
		n0 = Node(4)
		n1 = Node(1)
		n3 = Node(6)
		n2 = Node(5)
		n4 = Node(9)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		n3.append(n4)
		
		partitioned = partition_list(n0, 6)
		self.assertEqual(partitioned.data, 4)
		self.assertEqual(partitioned.next.data, 1)
		self.assertEqual(partitioned.next.next.data, 5)
		self.assertEqual(partitioned.next.next.next.data, 6)
		self.assertEqual(partitioned.next.next.next.next.data, 9)
		
if __name__ == '__main__':
	unittest.main()
	
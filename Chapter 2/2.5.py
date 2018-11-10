import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def add_nodes(l1, l2):
	sum_head, sum_tail = None, None
	carry = 0
	
	while (l1 and l2):
		sum_node = None
		sum = l1.data + l2.data + carry
		
		if (sum > 9):
			carry = sum // 10
			sum_node = Node(sum % 10)
		else:
			carry = 0
			sum_node = Node(sum)
			
		if sum_head:
			sum_tail.next = sum_node
			sum_tail = sum_tail.next
		else:
			sum_head, sum_tail = sum_node, sum_node
		
		l1 = l1.next
		l2 = l2.next
	
	return sum_head
		
	
class TestClass(unittest.TestCase):
	def test_add_nodes(self):
		n0 = Node(7)
		n1 = Node(1)
		n2 = Node(6)
		
		n0.append(n1)
		n1.append(n2)
		
		n3 = Node(5)
		n4 = Node(9)
		n5 = Node(2)
		
		n3.append(n4)
		n4.append(n5)
		
		summed = add_nodes(n0, n3)
		self.assertEqual(summed.data, 2)
		self.assertEqual(summed.next.data, 1)
		self.assertEqual(summed.next.next.data, 9)

		
if __name__ == '__main__':
	unittest.main()
	
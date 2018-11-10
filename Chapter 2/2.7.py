import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	

def check_palindrome(head):
	values = []
	while head:
		values.append(head.data)
		head = head.next
		
	start, end = 0, len(values)-1
	while (start < end):
		if (values[start] != values[end]):
			return False
		start += 1
		end -= 1
	return True
		
	
class TestClass(unittest.TestCase):
	def test_palindrome(self):
		n0 = Node(1)
		n1 = Node(2)
		n2 = Node(2)
		n3 = Node(1)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		
		self.assertEqual(check_palindrome(n0), True)
		
	def test_palindrome_odd(self):
		n0 = Node(1)
		n1 = Node(2)
		n2 = Node(3)
		n3 = Node(2)
		n4 = Node(1)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		n3.append(n4)
		
		self.assertEqual(check_palindrome(n0), True)
	
	def test_none(self):
		self.assertEqual(check_palindrome(None), True)
		
	def test_one(self):
		self.assertEqual(check_palindrome(Node(0)), True)
		
		
if __name__ == '__main__':
	unittest.main()
	
import unittest


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.head = None
		
	def pop(self):
		if (self.head != None):
			target = self.head.data
			self.head = self.head.next
			return target
		return None
		
	def push(self, val):
		n = Node(val)
		n.next = self.head
		self.head = n
		
	def peek(self):
		return self.head.data
		
	def isEmpty(self):
		return self.head is None
		

def sort(stk):
	stk2 = Stack()
	while not stk.isEmpty():
		count = 0
		curr = stk.pop()
		
		while not stk2.isEmpty() and stk2.peek() > curr:
			stk.push(stk2.pop())
			count += 1
		stk2.push(curr)
		
		# Can remove this loop
		while count > 0:
			stk2.push(stk.pop())
			count -= 1
	return stk2
	

class TestClass(unittest.TestCase):
	def test_sort(self):
		s = Stack()
		s.push(5)
		s.push(3)
		s.push(9)
		s.push(1)
		s.push(24)
		
		sorted_stack = sort(s)
		
		self.assertEqual(sorted_stack.pop(), 24)
		self.assertEqual(sorted_stack.pop(), 9)
		self.assertEqual(sorted_stack.pop(), 5)
		self.assertEqual(sorted_stack.pop(), 3)
		self.assertEqual(sorted_stack.pop(), 1)
	
	
if __name__ == '__main__':
	unittest.main()
			
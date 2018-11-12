import unittest


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self, val):
		self.head = Node(val)
		self.size = 1
		
	def pop(self):
		if (self.head != None):
			target = self.head.data
			self.head = self.head.next
			self.size -= 1
			return target
		return None
		
	def push(self, val):
		n = Node(val)
		n.next = self.head
		self.head = n
		self.size += 1
		

class SetOfStacks:
	def __init__(self, threshold):
		self.set_of_stacks = []
		self.threshold = threshold
		
	def s_push(self, val):
		if len(self.set_of_stacks) == 0:
			stk = Stack(val)
			self.set_of_stacks.append(stk)
			return
		
		curr_stack = self.set_of_stacks[-1]
		if curr_stack.size < self.threshold:
			curr_stack.push(val)
		else:
			stk = Stack(val)
			self.set_of_stacks.append(stk)
			
			
	def s_pop(self):
		curr_stack = self.set_of_stacks[-1]
		target = curr_stack.pop()
		if curr_stack.size == 0:
			del self.set_of_stacks[-1]
		return target
		
		
class TestClass(unittest.TestCase):
	def test_set_of_stacks(self):
		s = SetOfStacks(3)
		s.s_push(1)
		s.s_push(2)
		s.s_push(3)
		s.s_push(4)
		s.s_push(5)
		s.s_push(6)
		
		self.assertEqual(s.s_pop(), 6)
		self.assertEqual(s.s_pop(), 5)
		self.assertEqual(s.s_pop(), 4)
		self.assertEqual(s.s_pop(), 3)
		self.assertEqual(s.s_pop(), 2)
		self.assertEqual(s.s_pop(), 1)
		
		s.s_push(5)
		
		self.assertEqual(s.s_pop(), 5)
	
	
if __name__ == '__main__':
	unittest.main()
			
			

		
import unittest


class MyQueue:
	def __init__(self):
		self.in_stack = []
		self.out_stack = []
		
	def enqueue(self, val):
		self.in_stack.append(val)
		
	def dequeue(self):
		while self.in_stack:
			self.out_stack.append(self.in_stack.pop())
		target = self.out_stack.pop()
		while self.out_stack:
			self.in_stack.append(self.out_stack.pop())
		return target
	

class TestClass(unittest.TestCase):
	def test_myqueue(self):
		q = MyQueue()
		q.enqueue(1)
		q.enqueue(2)
		q.enqueue(3)
		
		self.assertEqual(q.dequeue(), 1)
		self.assertEqual(q.dequeue(), 2)
		self.assertEqual(q.dequeue(), 3)
	

if __name__ == '__main__':
	unittest.main()
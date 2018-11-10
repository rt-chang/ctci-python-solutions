import unittest


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode

		
class Stack:
	def __init__(self, val):
		self.head = Node(val)
		self.minimum = Node(val)
		
	def pop(self):
		if (self.head != None):
			target = self.head.data
			if (target == self.minimum.data):
				self.minimum = self.minimum.next
			self.head = self.head.next
			return target
		return None
		
	def push(self, val):
		if (val <= self.minimum.data):
			temp = self.minimum
			self.minimum = Node(val)
			self.minimum.append(temp)
		n = Node(val)
		n.next = self.head
		self.head = n
	
	def peek(self):
		return self.head.data
		
	def min(self):
		return self.minimum.data
	
		
class Queue:
	def __init__(self, head):
		self.head = head
		self.tail = head
		
	def dequeue(self):
		if (self.head != None):
			target = self.head.data
			self.head = self.head.next
			return target
		return None
		
	def enqueue(self, v):
		n = Node(v)
		if (self.head == None):
			self.head, self.tail = n, n
		else:
			self.tail.next = n
			self.tail = n
			
class TestClass(unittest.TestCase):
	def test_min(self):
		s = Stack(5)
		s.push(1)
		s.push(10)
		s.push(1)
		s.push(0)
		
		self.assertEqual(s.min(), 0)
		self.assertEqual(s.pop(), 0)
		self.assertEqual(s.pop(), 1)
		self.assertEqual(s.min(), 1)
		
if __name__ == '__main__':
	unittest.main()
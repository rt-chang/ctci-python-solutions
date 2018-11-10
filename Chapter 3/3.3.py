import unittest


class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next
		

class SetOfStacks:
	def __init__(self, data):
		self.setOfStacks = []
		self.head = Node(data, None)
		self.setOfStacks.append(self.head)
		self.curr_stack = self.setOfStacks[0]
		self.curr_count = 1
		
	def push(self, data):
		if (self.curr_count < 5):
			self.head = Node(data, self.head)
		
	def pop(self):
		
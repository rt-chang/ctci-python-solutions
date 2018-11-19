import unittest


class Node:
	def __init__(self, v):
		self.value = v
		self.edges = []
		
	def append(self, n):
		self.edges.append(n)
		

def has_route(root, target):
	visited = set()
	stack = [root]
	while stack:
		curr = stack.pop()
		if curr not in visited:
			if curr == target:
				return True
			visited.add(curr)
			for edge in curr.edges:
				stack.append(edge)
	return False
	

class TestClass(unittest.TestCase):
	def test_has_route(self):
		n0 = Node(0)
		n1 = Node(1)
		n2 = Node(2)
		n3 = Node(3)
		
		n0.append(n1)
		n0.append(n2)
		n2.append(n3)
		n3.append(n1)
		n2.append(n0)
		
		self.assertTrue(has_route(n0, n3))
		self.assertTrue(has_route(n0, n0))
		self.assertFalse(has_route(n1, n3))
		

if __name__ == "__main__":
	unittest.main()
	
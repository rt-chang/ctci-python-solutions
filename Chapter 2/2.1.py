import unittest

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def append(self, nextNode):
		self.next = nextNode
	
	
def remove_dupes(head):
	if (not head or head.next is None):
		return head
		
	seen = set()
	seen.add(head.data)
	
	sentinel, prev = head, head
	runner = head.next
	
	while (runner):
		if (runner.data in seen):
			prev.next = runner.next
		seen.add(runner.data)
		prev = prev.next
		runner = runner.next
	return sentinel
			
		
class TestRemoveDupes(unittest.TestCase):
	def test_remove_dupes(self):
		n0 = Node(0)
		n1 = Node(1)
		n2 = Node(1)
		n3 = Node(2)
		
		n0.append(n1)
		n1.append(n2)
		n2.append(n3)
		
		remove_dupes(n0)
		self.assertEqual(n0.next, n1)
		self.assertEqual(n1.next, n3)
		
	def test_remove_dupes_empty(self):
		self.assertEqual(remove_dupes(None), None)
		
	def test_remove_dupes_one_node(self):		
		n0 = Node(0)
		self.assertEqual(remove_dupes(n0), n0)
		
if __name__ == '__main__':
	unittest.main()
	
import unittest


class Node:
	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right
		

def max_depth(node):
	if not node:
		return 0
	
	left_height = max_depth(node.left) + 1
	right_height = max_depth(node.right) + 1
	return max(left_height, right_height)
		

def is_balanced(root):
	if not root:
		return True
		
	left_height = max_depth(root.left)
	right_height = max_depth(root.right)
	if (abs(left_height - right_height) <= 1):
		return is_balanced(root.left) and is_balanced(root.right)
	return False
	

class TestClass(unittest.TestCase):
	def test_is_balanced(self):
		'''
				   Node
					/  \
			Node    Node
			   /         /
		 Node      Node
		'''
		root = Node(Node(Node()), Node(Node()))
		self.assertTrue(is_balanced(root))		
		'''
					   Node
						/  \
				Node    Node
				 /             \
		  Node             Node
      		  /                  \
		Node                  Node
		'''
		root = Node(Node(Node(Node())), Node(None, Node(None, Node())))
		self.assertFalse(is_balanced(root))
		
		
if __name__ == '__main__':
	unittest.main()
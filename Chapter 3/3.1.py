import unittest


class Array3Stack:
	def __init__(self):
		self.array = [None for _ in range(3)]
		self.curr_index = [0, 1, 2]
		
	def pop(self, stack):
		if (stack not in [0, 1, 2]):
			raise Exception("Not a valid stack number")
		if (self.curr_index[stack]> 2):
			self.curr_index[stack] -= 3
		target = self.array[self.curr_index[stack]]
		self.array[self.curr_index[stack]] = None
		return target
		
	def push(self, stack, value):
		if (stack not in [0, 1, 2]):
			raise Exception("Not a valid stack number")
		if (self.curr_index[stack] >= len(self.array)):
			self.array += [None for _ in range(3)]
		self.array[self.curr_index[stack]] = value
		self.curr_index[stack] += 3
		print(self.array)
		
	
class TestClass(unittest.TestCase):
	def test_array_3_stack(self):
		a = Array3Stack()
		a.push(0, 1)
		a.push(0, 2)
		a.push(1, 10)
		a.push(0, 3)
		
		self.assertEqual(a.pop(0), 3)
		self.assertEqual(a.pop(0), 2)
		self.assertEqual(a.pop(0), 1)
		self.assertEqual(a.pop(1), 10)
		self.assertEqual(a.pop(0), None)
		
if __name__ == '__main__':
	unittest.main()
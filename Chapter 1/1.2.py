import unittest

def reverse(str_list):
	start = 0
	end = len(str_list) - 1
	while (start < end):
		str_list[start], str_list[end] = str_list[end], str_list[start]
		start += 1
		end -= 1
	return str_list
		
class TestReverseStr(unittest.TestCase):
	def test_reverse(self):
		self.assertEqual(reverse(["y","e","s"]), ["s","e","y"])
		self.assertEqual(reverse(["y"]), ["y"])
		self.assertEqual(reverse([]), [])
		
if __name__ == '__main__':
	unittest.main()
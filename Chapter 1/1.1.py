import unittest

def all_unique_char(str):
	seen = set()
	for c in str:
		if (c in seen):
			return False
		seen.add(c)
	return True
		
class TestAllUniqueChar(unittest.TestCase):
	def test_unique(self):
		self.assertTrue(all_unique_char("yes"))
		self.assertFalse(all_unique_char("llama"))
		
if __name__ == '__main__':
	unittest.main()
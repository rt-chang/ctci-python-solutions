import unittest

def is_permutation(str1, str2):
	if (len(str1) != len(str2)):
		return False
		
	seen_count = {}
	for c in str1:
		if (c in seen_count):
			seen_count[c] += 1
		else:
			seen_count[c] = 1
	
	for c in str2:
		if (c not in seen_count or seen_count[c] == 0):
			return False
		seen_count[c] -= 1
	return True
		
class TestIsPermutation(unittest.TestCase):
	def test_is_permutation(self):
		self.assertTrue(is_permutation("hello", "olhel"))
		self.assertTrue(is_permutation("", ""))
		self.assertFalse(is_permutation("bye", "by"))
		
if __name__ == '__main__':
	unittest.main()
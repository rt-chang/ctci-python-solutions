import unittest

def compress(str1):
	str1_len = len(str1)
	if (str1_len == 0):
		return ""
	
	if (str1_len == 1):
		return str
		
	compressed_str = ""
	current_char = str1[0]
	current_count = 1
	for c in str1[1:]:
		if (c == current_char):
			current_count += 1
		else:
			compressed_str += current_char
			compressed_str += str(current_count)
			current_char = c
			current_count = 1
	compressed_str += current_char
	compressed_str += str(current_count)
	
	if (len(compressed_str) > str1_len):
		return str1
	return compressed_str
	
		
class TestCompress(unittest.TestCase):
	def test_compress(self):
		self.assertEqual(compress("aabcccccaaa"), "a2b1c5a3")
		self.assertEqual(compress(""), "")
		self.assertEqual(compress("bye"), "bye")
		
if __name__ == '__main__':
	unittest.main()